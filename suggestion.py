import pandas as pd
from openai.embeddings_utils import get_embedding,cosine_similarity
from decouple import config
import openai
from mongodbfetch import connection, fetch_embeddings

api_key = config('OPENAI_API_KEY')
openai.api_key = api_key

# 
# customer_order_data = [
#     {
#         "pain_points": "As a solo entrepreneur, I struggle with managing multiple tasks and staying organized. I often find it challenging to prioritize my work and keep track of deadlines.",
#         "goals": "My goal is to improve my productivity and efficiency as a solo entrepreneur. I want to streamline my workflow, automate repetitive tasks, and have a better overview of my projects.",
#         "requirements": "I would love a micro SaaS that offers task management, project tracking, and reminders. Integration with popular productivity tools like email and calendar would be a plus.",
#     }
# ]
def get_embeddings_from_customer_data(customer_order_data):

    customer_order_df = pd.DataFrame(customer_order_data)
    # customer_order_df['combined'] = customer_order_df.apply(lambda row: f"{row['pain_points']}, {row['goals']}, {row['requirements']}", axis=1)
    customer_order_df['combined'] = customer_order_df.apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)
    customer_order_df['text_embedding'] = customer_order_df.combined.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

    return customer_order_df

def get_similar_ideas(customer_order_data):
    embeddings_customer_question = get_embeddings_from_customer_data(customer_order_data)['text_embedding'].values[0]

    product_data_df = fetch_embeddings()

    product_data_df['search_products'] = product_data_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    product_data_df = product_data_df.sort_values('search_products', ascending=False)
    top_products = product_data_df.head(5)

    results = []
    for index, row in top_products.iterrows():
        result = {
            'product_name': row['name'],
            'product_score': row['search_products']
        }
        results.append(result)

    return results


__all__ = ['get_similar_ideas', 'get_embeddings_from_customer_data']