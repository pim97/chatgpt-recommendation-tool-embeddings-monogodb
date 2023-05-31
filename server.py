#!/usr/bin/python3

# Flask
import logging
import json
import sys
from flask import Flask
from flask import request
from flask import abort
from urllib.parse import urlparse
from suggestion import get_embeddings_from_customer_data, get_similar_ideas
from flask_cors import CORS  # Import CORS from flask_cors
from mongodbfetch import fetch_by_name
from bson import json_util

app = Flask(__name__)

CORS(app) 

@app.route('/', methods=['GET'])
def get():
    return 'Hello, World!'

@app.route('/recommend', methods=['POST'])
def index():
    user_fields = request.json
    top_ideas = get_similar_ideas(user_fields)
    extra = []
    for idea in top_ideas:
        product_name = idea['product_name']
        fetched_data = fetch_by_name(product_name)
        # fetched_data['_id'] = str(fetched_data['_id'])
        extra.append(fetched_data)
    try:

        return json.dumps({
                'ideas': top_ideas,
                'details': extra
            },default=json_util.default)

    except Exception as e:
        print(f"Error: {e}")
        return str(e)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=sys.argv[1])