from flask import request
from flask_restplus import Resource, fields
from flask_restplus import Namespace

from api.main.service.enrichment_service import enrich_with_author
from core_search.search import Search
from flask import  current_app

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
        data = []
        current_app.logger.debug("Searching for matching summaries")
        for query in queries:
            matched_summaries = search.search_summaries(query, size)
            for summary in matched_summaries:
                summary["query"] = query
            data.append(matched_summaries)
        current_app.logger.debug("Enriching summaries with author")
        return enrich_with_author(data)
