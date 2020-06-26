from api.main.service.enrichment_service import enrich_with_author, get_author
from api.test.test_data.data import AUTHOR_ENRICHMENT_DATA, AUTHOR_DATA


def test001_author_enrichment():
    mock_test_data = AUTHOR_ENRICHMENT_DATA
    for data in mock_test_data[0]:
        del data["author"]
    results = enrich_with_author(mock_test_data)
    for actual, result in zip(mock_test_data[0], results[0]):
        assert actual["id"] == result["id"]
        assert actual["author"] == result["author"]


def test002_get_author():
    mock_data = AUTHOR_DATA
    for data in mock_data:
        assert data["author"] == get_author(data["id"]).json()["author"]


