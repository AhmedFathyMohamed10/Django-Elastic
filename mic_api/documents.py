from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry


# Define the Elasticsearch index
drug_index = Index('drugs')

@drug_index.document
class DrugDocument(Document):
    class Django:
        # The name of the MongoDB collection
        model = 'drugs_coll'

    class Index:
        name = 'drugs'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    # Fields that i want to index in Elasticsearch
    brand_name = fields.TextField(attr='openfda.brand_name')
    generic_name = fields.TextField(attr='openfda.generic_name')