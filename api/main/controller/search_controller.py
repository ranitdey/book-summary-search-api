from flask import request
from flask_restplus import Resource, fields
from flask_restplus import Namespace

from core_search.search import Search

api = Namespace('search', description='search book summaries')
_search_summary = api.model('search', {
    'queries': fields.List(fields.String, required=True),
    'size': fields.Integer(required=True),
})

search = Search()


@api.route('/search')
class SearchSummaries(Resource):

    @api.response(200, "Successfully fetched search results")
    @api.doc('search summary')
    @api.expect(_search_summary, validate=True)
    def post(self):
        """Searches for matching summaries"""
        queries = request.json["queries"]
        size = request.json["size"]
        return search.search_summaries(queries[0], size)
