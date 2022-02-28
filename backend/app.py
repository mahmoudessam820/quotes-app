import json
from flask import (Flask, jsonify)
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def handle_files_data():
    return load_data('images.json'), load_data('quotes.json')


def clear_nulls():
    images, quotes = handle_files_data()
    new_images = {}
    new_quotes = {}
    for author in images.keys():
        if images[author]:
            new_images[author] = images[author]
            new_quotes[author] = quotes[author]
    return new_images, new_quotes

# Extract authors names and make list of authors.
def create_author_list(authors):
    return [authors[i] for i in range(0, len(authors))]


@app.route('/')
def home():
    images, quotes = clear_nulls()
    authors = list(quotes.keys())
    authors_list = create_author_list(authors)
    return jsonify(
        images=images,
        quotes=quotes,
        authors=authors_list
    )
