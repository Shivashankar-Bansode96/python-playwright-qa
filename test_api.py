
from playwright.sync_api import Playwright, expect


def test_get_post(playwright: Playwright):
    request = playwright.request.new_context()

    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"]

    request.dispose()


import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def api_request(playwright: Playwright):
    request = playwright.request.new_context()
    yield request
    request.dispose()


def test_get_post(api_request):
    response = api_request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert data["title"]


def test_get_nonexistent_post(api_request):
    response = api_request.get(
        "https://jsonplaceholder.typicode.com/posts/999999"
    )

    assert response.status == 404
    assert response.text() == "{}"