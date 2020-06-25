"""
Author: Ranit Dey
Description: This class enables users to perform search query against the dataset.Also this class is responsible to
             create and load inverted index instance with initial dataset.
"""
from core_search.constants import DATA_PATH
from core_search.lib.file_utils import read
from core_search.lib.inverted_index import InvertedIndex
from core_search.lib.levenshtein import levenshtein_ratio, levenshtein_partial_ratio
from core_search.lib.preprocessor import tokenize


class Search:

    def __init__(self):
        self.inverted_index = InvertedIndex()
        self.data = read(DATA_PATH)["summaries"]
        self.inverted_index.load(self.data)
        self.map = {}
        for summery in self.data:
            self.map[summery["id"]] = summery["summary"]

    def search_summaries(self, query, size):
        query = query.lower()
        tokens = tokenize(query)
        matching_docs = self.inverted_index.get_matching_documents(tokens)
        ranked_docs = self.rank_by_levenshtein_distance(query, matching_docs)
        response = []
        for doc in ranked_docs:
            response.append({
                "summary": self.map[doc["id"]],
                "id": doc["id"]
            })
        return response[:min(size, len(response))]

    def rank_by_levenshtein_distance(self, query, docs):
        docs_with_distance = []
        for doc in docs:
            docs_with_distance.append({"id": doc,
                                       "similarity": levenshtein_ratio(self.map[doc], query)})
        return sorted(docs_with_distance, key=lambda obj: obj["similarity"], reverse=True)
