import json
from re import A 
import requests
from bs4 import BeautifulSoup


# Get the data from the API
def get_data():
    url = 'https://type.fit/api/quotes'
    response = requests.get(url)
    return response.json()

# Handle the quotes data and filter the data to avoid the null author
def quotes_data(api_data):
    quotes = {}
    for data in api_data:
        if data['author']:
            if not data['author'] in quotes:
                quotes[data['author']] = []
            quotes[data['author']].append(data['text'])
    return quotes

'''
    Here we will go to Wikipedia to search about the author image.
    And if we find it will extract the author image by the class name.
    We use the BeautifulSoup library to parse the Wikipedia page and extract the class name.
'''
def get_author_image(author):
    url = f'https://en.wikipedia.org/wiki/{author}'
    page = requests.get(url)
    html_doc = page.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        td = soup.find('td', class_ = 'infobox-image')
        image = td.find('img')
        return 'https://' + image['src']
    except Exception as e:
        print(e)
        return None


def handle_author_images(authors):
    images = {}
    numbers_authors = len(authors)
    for index, author in enumerate(authors):
        images[author] = get_author_image(author)
        print(f'processing {index}/{author} author')
    return images


def create_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    api_data = get_data()
    quotes   = quotes_data(api_data)
    author   = list(quotes.keys())
    images   = handle_author_images(author)
    create_json_file('quotes.json', quotes)
    create_json_file('images.json', images)