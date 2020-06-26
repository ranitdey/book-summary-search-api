"""
Author: Ranit Dey
Description: Inverted index data structure
"""
from ..library.preprocessor import *


class InvertedIndex:

    def __init__(self):
        self.container = {}

    def add_token(self, token, document_id):
        token = make_alphanumeric(token)
        if token in self.container:
            self.container[token].append(document_id)
        else:
            self.container[token] = [document_id]

    def get_matching_documents(self, tokens):
        data = []
        for token in tokens:
            if token in self.container:
                for doc in self.container[token]:
                    data.append(doc)
        return set(data)

    def load(self, data):
        for ele in data:
            processed_data = tokenize(ele["summary"].lower())
            for token in processed_data:
                self.add_token(token, ele["id"])
