
import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.fixture
def api_request(playwright: Playwright):
    request = playwright.request.new_context()
    yield request
    request.dispose()


def test_api_get_post(api_request):
    response = api_request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"]


def test_ui_valid_login(page: Page):
    page.goto(
        "https://practicetestautomation.com/practice-test-login/"
    )

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page).to_have_url(
        "https://practicetestautomation.com/logged-in-successfully/"
    )

    expect(
        page.get_by_text(
            "Congratulations student. You successfully logged in!"
        )
    ).to_be_visible()
