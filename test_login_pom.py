
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_USERNAME_ERROR,
    INVALID_PASSWORD_ERROR,
)


def test_valid_login_pom(login_page: LoginPage, page: Page):
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url(
        "https://practicetestautomation.com/logged-in-successfully/"
    )

    expect(
        page.get_by_text(
            "Congratulations student. You successfully logged in!"
        )
    ).to_be_visible()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            INVALID_USERNAME,
            INVALID_PASSWORD,
            INVALID_USERNAME_ERROR,
        ),
        (
            VALID_USERNAME,
            INVALID_PASSWORD,
            INVALID_PASSWORD_ERROR,
        ),
        (
            "",
            VALID_PASSWORD,
            INVALID_USERNAME_ERROR,
        ),
    ],
)
def test_invalid_login_pom(
    login_page: LoginPage,
    username: str,
    password: str,
    expected_error: str,
):
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)


