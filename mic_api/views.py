# Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient, IndexModel, TEXT
from pymongo.errors import PyMongoError
import re
import logging
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

logger = logging.getLogger(__name__)


# MongoDB Configuration
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'mic_db'
COLLECTION_NAME = 'drugs_coll'

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Drop existing indexes to avoid conflicts
collection.drop_indexes()

# Create text search index for text searching 
indexes = [
    IndexModel([
        ('openfda.brand_name', TEXT),
        ('openfda.generic_name', TEXT),
    ], name='text_search_index'),
]
collection.create_indexes(indexes)




# Elasticsearch client
es = Elasticsearch()


# --------------SEARCHING-----------------------------------------
def construct_query(search_terms, filters=None):
    should_clauses = []
    for term in search_terms:
        should_clauses.append({"match": {"brand_name": {"query": term, "fuzziness": "AUTO"}}})
        should_clauses.append({"match": {"generic_name": {"query": term, "fuzziness": "AUTO"}}})
    
    query = {
        "bool": {
            "should": should_clauses,
            "minimum_should_match": 1  # at least one should match
        }
    }

    if filters:
        filter_clauses = []
        for key, value in filters.items():
            filter_clauses.append({"term": {key: value}})
        
        query['bool']['filter'] = filter_clauses
    
    return query


PAGE_SIZE = 10
@api_view(['GET'])
def product_list(request):
    try:
        search = request.GET.get('search', '')
        page = int(request.GET.get('page', 1))

        s = Search(using=es, index='drugs')
        if search:
            s = s.query("multi_match", query=search, fields=['openfda.brand_name', 'openfda.generic_name'], fuzziness='AUTO')

        total_count = s.count()
        start = (page - 1) * PAGE_SIZE
        s = s[start:start + PAGE_SIZE]
        response = s.execute()

        results = [hit.to_dict() for hit in response]
        total_pages = (total_count + PAGE_SIZE - 1) // PAGE_SIZE

        response_data = {
            'results': results,
            'total_count': total_count,
            'page': page,
            'total_pages': total_pages,
            'page_size': PAGE_SIZE
        }
        # print("Search query: %s", search)
        # print("Elasticsearch query: %s", s.to_dict())
        # print("Elasticsearch response: %s", response.to_dict())

        return Response(response_data)

    except Exception as e:
        logger.error("Error occurred during search: %s", e)
        return Response({'error': str(e)}, status=500)

# ---------------END OF SEARCHING --------------------------------

# -------------PRODUCT (DRUG) DETAILS-----------------------------
@api_view(['GET'])
def product_detail(request, set_id):
    try:
        product = collection.find_one({'set_id': set_id}, {'_id': 0})
        if product:
            return Response(product)
        else:
            return Response({'error': 'Product not found'}, status=404)

    except PyMongoError as e:
        return Response({'error': str(e)}, status=500)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# ----------------------------------------------------------------

# -------------FILTERATIONS---------------------------------------
@api_view(['GET'])
def distinct_values(request):
    try:
        generic_names = collection.distinct('openfda.generic_name')
        brand_names = collection.distinct('openfda.brand_name')
        manufacturers = collection.distinct('openfda.manufacturer_name')
        application_numbers = collection.distinct('openfda.application_number')
        versions = collection.distinct('version')

        response_data = {
            'generic_names': generic_names,
            'brand_names': brand_names,
            'manufacturers': manufacturers,
            'application_numbers': application_numbers,
            'versions': versions,
        }

        return Response(response_data)

    except PyMongoError as e:
        return Response({'error': str(e)}, status=500)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# -------------END OF FILTERATION----------------------------------

# -----------------------------------------------------------------

# ---------------DRUG-DRUG INTERACTIONS ---------------------------
def fetch_interactions(drug_name):
    logger.debug(f'Fetching interactions for: {drug_name}')
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"openfda.generic_name": drug_name}},
                    {"match": {"openfda.brand_name": drug_name}}
                ]
            }
        }
    }
    result = es.search(index="drugs", body=query)
    logger.debug(f'Elasticsearch result for {drug_name}: {result}')

    if not result['hits']['hits']:
        return [], f'{drug_name} not found in the database.'

    drug_doc = result['hits']['hits'][0]['_source']
    interactions_set = set()

    if 'Rxdata' in drug_doc:
        # Ensure 'Rxdata' has at least one item
        rxdata_item = drug_doc['Rxdata']
        if rxdata_item and isinstance(rxdata_item, list) and len(rxdata_item) > 0:
            interactionTypeGroup = rxdata_item[0].get('interactionTypeGroup', [{}])
            
            # Ensure 'interactionTypeGroup' has at least one item
            if interactionTypeGroup and isinstance(interactionTypeGroup, list) and len(interactionTypeGroup) > 0:
                interactionType = interactionTypeGroup[0].get('interactionType', [{}])
                
                # Ensure 'interactionType' has at least one item
                if interactionType and isinstance(interactionType, list) and len(interactionType) > 0:
                    interactionPair = interactionType[0].get('interactionPair', [])
                    
                    # Ensure 'interactionPair' is a list
                    if isinstance(interactionPair, list):
                        for interaction in interactionPair:
                            description = interaction.get('description', 'No description available')
                            interactionConcepts = interaction.get('interactionConcept', [])
                            
                            # Ensure 'interactionConcept' is a list
                            if isinstance(interactionConcepts, list):
                                for concept in interactionConcepts:
                                    # Check 'sourceConceptItem' and its 'name'
                                    minConceptItem = concept.get('minConceptItem', {})
                                    if isinstance(minConceptItem, dict):
                                        min_name = minConceptItem.get('name', '').lower()
                                        if min_name:
                                            interactions_set.add((min_name, description))
                                        else:
                                            logger.debug(f'Missing minConceptItem name in {concept}')
                                    else:
                                        logger.debug(f'Missing minConceptItem in {concept}')
                            else:
                                logger.debug(f'Expected list for interactionConcepts but got {type(interactionConcepts)}')
                else:
                    logger.debug('No valid interactionType found in interactionTypeGroup')
            else:
                logger.debug('No valid interactionTypeGroup found in Rxdata')
        else:
            logger.debug('No valid Rxdata found in drug_doc')
    else:
        logger.debug('No Rxdata found in drug_doc')


    interactions_list = [{'name': name, 'description': description} for name, description in interactions_set]
    logger.debug(f'Interactions for {drug_name}: {interactions_list}')
    return interactions_list, None


@api_view(['POST'])
def check_drug_interactions(request):
    try:
        drugs = [drug.strip().lower() for drug in request.data.get('drugs', [])]

        if not drugs:
            return Response({'error': 'Please provide at least one drug.'}, status=400)

        interaction_details = []
        interaction_message = ''

        if len(drugs) == 1:
            drug1_interactions, message = fetch_interactions(drugs[0])
            if message:
                return Response({'interactions': False, 'message': message})

            return Response({
                'interactions': True,
                'drug_interactions': drug1_interactions,
                'drug1_length': len(drug1_interactions),
                'message': f'{drugs[0]} interactions found. Total: {len(drug1_interactions)}.'
            })

        all_drug_interactions = {}
        for drug in drugs:
            drug_interactions, message = fetch_interactions(drug)
            if message:
                interaction_message += message + ' '
            all_drug_interactions[drug] = drug_interactions

        for i, drug1 in enumerate(drugs):
            for drug2 in drugs[i + 1:]:
                drug1_interactions = all_drug_interactions.get(drug1, [])
                drug2_interactions = all_drug_interactions.get(drug2, [])

                if drug1_interactions and drug2_interactions:
                    for interaction in drug1_interactions:
                        if interaction['name'] == drug2:
                            interaction_details.append({
                                'drug1': drug1,
                                'drug2': drug2,
                                'description': interaction['description']
                            })
                    for interaction in drug2_interactions:
                        if interaction['name'] == drug1:
                            interaction_details.append({
                                'drug1': drug2,
                                'drug2': drug1,
                                'description': interaction['description']
                            })
                else:
                    logger.debug(f'No interactions found for {drug1} or {drug2}')

        if interaction_details:
            return Response({
                'interactions': True,
                'details': interaction_details,
                'message': 'Interactions found between the selected drugs.'
            })
        else:
            return Response({'interactions': False, 'message': interaction_message.strip() or 'No drug ⬌ drug interactions were found between the drugs in your list. However, this does not necessarily mean no drug interactions exist. Always consult your healthcare provider.'})

    except Exception as e:
        logger.error(f'Error checking drug interactions: {e}')
        return Response({'error': str(e)}, status=500)

# ----------------END OF DRUG ERUG INTERACTIONS --------------------