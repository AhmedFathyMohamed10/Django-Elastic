# @api_view(['POST'])
# def check_drug_interactions(request):
#     try:
#         drugs = [drug.strip().lower() for drug in request.data.get('drugs', [])]

#         if not drugs:
#             return Response({'error': 'Please provide at least one drug.'}, status=400)

#         interaction_details = []
#         interaction_message = ''

#         def fetch_interactions(drug_name):
#             logger.debug(f'Fetching interactions for: {drug_name}')
#             query = {
#                 "query": {
#                     "bool": {
#                         "should": [
#                             {"match": {"openfda.generic_name": drug_name}},
#                             {"match": {"openfda.brand_name": drug_name}}
#                         ]
#                     }
#                 }
#             }
#             result = es.search(index="drugs", body=query, fuzziness='AUTO')
#             if not result['hits']['hits']:
#                 return [], f'{drug_name} not found in the database.'

#             drug_doc = result['hits']['hits'][0]['_source']
#             interactions_set = set()
#             if 'Rxdata' in drug_doc:
#                 for interactionTypeGroup in drug_doc['Rxdata']:
#                     for interactionType in interactionTypeGroup.get('interactionTypeGroup', []):
#                         for interactionPair in interactionType.get('interactionType', []):
#                             for interaction in interactionPair.get('interactionPair', []):
#                                 description = interaction.get('description', 'No description available')
#                                 for interactionConcept in interaction.get('interactionConcept', []):
#                                     interaction_name = interactionConcept['minConceptItem']['name'].lower()
#                                     interactions_set.add((interaction_name, description))

#             interactions_list = [{'name': name, 'description': description} for name, description in interactions_set]
#             return interactions_list, None

#         if len(drugs) == 1:
#             drug1_interactions, message = fetch_interactions(drugs[0])
#             if message:
#                 return Response({'interactions': False, 'message': message})

#             return Response({
#                 'interactions': True,
#                 'drug_interactions': drug1_interactions,
#                 'message': f'{drugs[0]} interactions found. Total: {len(drug1_interactions)}.'
#             })

#         all_drug_interactions = {}
#         for drug in drugs:
#             drug_interactions, message = fetch_interactions(drug)
#             if message:
#                 interaction_message += message + ' '
#             all_drug_interactions[drug] = drug_interactions

#         for i, drug1 in enumerate(drugs):
#             for drug2 in drugs[i + 1:]:
#                 drug1_interactions = all_drug_interactions.get(drug1, [])
#                 drug2_interactions = all_drug_interactions.get(drug2, [])

#                 if drug1_interactions and drug2_interactions:
#                     for interaction in drug1_interactions:
#                         if interaction['name'] == drug2:
#                             interaction_details.append({
#                                 'drug1': drug1,
#                                 'drug2': drug2,
#                                 'description': interaction['description']
#                             })
#                     for interaction in drug2_interactions:
#                         if interaction['name'] == drug1:
#                             interaction_details.append({
#                                 'drug1': drug2,
#                                 'drug2': drug1,
#                                 'description': interaction['description']
#                             })
#                 else:
#                     logger.debug(f'No interactions found for {drug1} or {drug2}')

#         if interaction_details:
#             return Response({
#                 'interactions': True,
#                 'details': interaction_details,
#                 'message': f'Interactions found between the selected drugs.'
#             })
#         else:
#             return Response({'interactions': False, 'message': interaction_message.strip() or 'No drug ⬌ drug interactions were found between the drugs in your list. However, this does not necessarily mean no drug interactions exist. Always consult your healthcare provider.'})

#     except Exception as e:
#         logger.error(f'Error checking drug interactions: {e}')
#         return Response({'error': str(e)}, status=500)