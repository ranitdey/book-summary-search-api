"""
Author: Ranit Dey
Description: Inverted index data structure
"""

import re


class InvertedIndex:
    pattern = re.compile('[\W_]+')

    def __init__(self):
        self.container = {}

    def add_token(self,token,document_id):
        token = self.make_alphanumeric(token)
        if token in self.container:
            self.container[token].add(document_id)
        else:
            self.container[token] = [document_id]

    def make_alphanumeric(self,target):
        return InvertedIndex.pattern.sub("", target)

    def get_matching_documents(self,token):
        if token in self.container:
            return self.container[token]
        else:
            return []
