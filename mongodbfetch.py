from pymongo import MongoClient
import pandas as pd
from decouple import config

def connection(database = 'saas_data', collection = 'saas_data_vectors'):
    # Connect to MongoDB
    client = MongoClient(config('MONGO_CONNECTION_STRING'))
    db = client[database]
    collection = db[collection]
    return {
        'client': client,
        'db': db,
        'collection': collection
    }

# Fetch a single document
def fetch_by_name(name_to_search):
    connection_info = connection(collection='saas_data')
    client, db, collection = connection_info['client'], connection_info['db'], connection_info['collection']

    # Construct the query filter
    query = {"name": name_to_search}

    # Find the first document that matches the query filter
    document = collection.find_one(query)

    # Process the found document
    if document:
        return document
    else:
        return "No document found"

# Fetch all documents
def fetch_embeddings():
    connection_info = connection()
    client, db, collection = connection_info['client'], connection_info['db'], connection_info['collection']

    # Fetch all documents from the collection
    documents = collection.find()

    # Create an empty list to store the fetched data
    fetched_data = []

    # Iterate over the documents and extract the required fields
    for document in documents:
        fetched_item = {
            'name': document['name'],
            'text_embedding': document['text_embedding']
        }
        fetched_data.append(fetched_item)

    # Create a new dataframe with the fetched data
    fetched_data_df = pd.DataFrame(fetched_data)
    return fetched_data_df


__all__ = ['connection', 'fetch_embeddings', 'fetch_by_name']