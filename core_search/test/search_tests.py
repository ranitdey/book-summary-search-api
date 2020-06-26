from core_search.test.data.search_data import TEST_DATA_SEARCH
from core_search.search import Search
import logging

LOGGER = logging.getLogger(__name__)


def test001_search_validation_exact_match():
    mock_data = TEST_DATA_SEARCH
    search = Search()
    for data in mock_data:
        LOGGER.info("Processing query for id %s" % data["id"])
        result = search.search_summaries(data["query"], 4)
        assert len(result) == 4
        assert result[0]["id"] == data["id"]


def test002_search_validation_partial_match():
    mock_data = TEST_DATA_SEARCH
    search = Search()
    for data in mock_data:
        LOGGER.info("Processing query for id %s" % data["id"])
        query = data["query"]
        result = search.search_summaries(query[0:len(query)//2], 4)
        assert len(result) == 4
        assert result[0]["id"] == data["id"]


