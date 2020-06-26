import requests
from flask import current_app


def enrich_with_author(data):
    cache = {}
    for query_list in data:
        for query in query_list:
            if query["id"] in cache:
                query["author"] = cache[query["id"]]
            else:
                response = get_author(query["id"])
                if response.status_code == 200:
                    author = response.json()["author"]
                    cache[query["id"]] = author
                    query["author"] = author
    return data


def get_author(book_id):
    url = current_app.config["AUTHOR_SERVICE"]
    response = requests.post(url, json={"book_id": book_id})
    if response.status_code != 200:
        current_app.logger.error("Author details not found for book id %s" % book_id)
    return response



