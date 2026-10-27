import pytest
from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
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
        page.get_by_text("Congratulations student. You successfully logged in!")
    ).to_be_visible()

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("wronguser", "WrongPassword123", "Your username is invalid!"),
        ("student", "WrongPassword123", "Your password is invalid!"),
        ("", "Password123", "Your username is invalid!"),
        ("invaliduser", "Password123", "Your username is invalid!"),
    ],
)
def test_invalid_login(
    page: Page,
    username: str,
    password: str,
    expected_error: str,
):
    page.goto(
        "https://practicetestautomation.com/practice-test-login/"
    )

    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#error")).to_have_text(expected_error)

def test_page_title(page: Page):
    page.goto(
        "https://practicetestautomation.com/practice-test-login/"
    )

    expect(page).to_have_title("Test Login | Practice Test Automation")