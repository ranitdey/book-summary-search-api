"""
Author: Ranit Dey
Description: Inverted index data structure
"""
from core_search.matcher.preprocessor import *


class InvertedIndex:

    def __init__(self):
        self.container = {}

    def add_token(self, token, document_id):
        token = make_alphanumeric(token)
        if token in self.container:
            self.container[token].add(document_id)
        else:
            self.container[token] = [document_id]

    def get_matching_documents(self,token):
        if token in self.container:
            return self.container[token]
        else:
            return []

    def load(self, data):
        for ele in data:
            processed_data = tokenize(cleanup_punctuation(ele["summary"]).lower())
            for token in processed_data:
                self.add_token(token, ele["id"])
