import json

from manage import app


def test001_search_route():
    client = app.test_client()
    url = "/api/v1/search"
    mock_data = {
        "queries": ["in your l", "is your problems", "I should do"],
        "size": 3
    }
    response = client.post(url, data=json.dumps(mock_data), headers={'Content-Type': 'application/json'})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data["results"]) == 3
    for result in data["results"]:
        assert len(result) == 3
        for summary in result:
            assert "author" in summary
            assert "query" in summary
            assert "id" in summary
            assert "summary" in summary


def test002_search_route_bad_payload():
    client = app.test_client()
    url = "/api/v1/search"
    mock_data = {
        "queries": "in your l",
        "size": 3
    }
    response = client.post(url, data=json.dumps(mock_data), headers={'Content-Type': 'application/json'})
    assert response.status_code == 400


def test003_search_route_empty_query():
    client = app.test_client()
    url = "/api/v1/search"
    mock_data = {
        "queries": [],
        "size": 3
    }
    response = client.post(url, data=json.dumps(mock_data), headers={'Content-Type': 'application/json'})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data["results"]) == 0
