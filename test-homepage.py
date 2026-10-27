
from playwright.sync_api import Page, expect


def test_playwright_heading(page: Page):
    page.goto("https://playwright.dev/")

    heading = page.get_by_role("heading", level=1)

    expect(heading).to_be_visible()

    print("Heading found:", heading.inner_text())
