import pytest
from fastapi.testclient import TestClient
from league_ranker.api import app


def test_rank_api():
    client = TestClient(app)
    response = client.post("/rank", json={"matches": [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0"
    ]})
    assert response.status_code == 200
    assert "ranking" in response.json()
    assert response.json()["ranking"][0].startswith("1. Tarantulas")

