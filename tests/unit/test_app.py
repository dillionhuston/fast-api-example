from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from fast_api_example.app import app


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client


def test_should_return_static_response_from_api_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.json() == {"Hello": "World"}


def test_should_return_read_item(client: TestClient) -> None:
    response = client.get("/items/1234", params={"query": "test"})
    assert response.json() == {"item_id": 1234, "query": "test"}
