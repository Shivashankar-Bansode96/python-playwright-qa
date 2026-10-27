
from playwright.sync_api import Page


class LoginPage:
    def get_error_message(self) -> str:
        return self.error_message.inner_text()
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role(
            "button", name="Submit"
        )
        self.error_message = page.locator("#error")

    def open(self):
        self.page.goto(
            "https://practicetestautomation.com/practice-test-login/"
        )

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
