from flask_restplus import Api

from .search_controller import api as ns1

api = Api(
    title='Search summaries',
    version='library.0',
    description='Given a query search matching summaries',
)

api.add_namespace(ns1, path="/api/v1")
