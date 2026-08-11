from typing import TYPE_CHECKING
from playwright.sync_api import Page

if TYPE_CHECKING:
    from pages.secure_page import SecurePage


class LoginPage:
    """Page object for the Login page of The Internet application."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username = self.page.locator("input#username")
        self.password = self.page.locator("input#password")
        self.login_button = self.page.locator("button[type=\"submit\"]")

    def navigate(self) -> None:
        self.page.goto(f"{self.base_url}/login")

    def enter_username(self, username: str) -> None:
        self.username.fill(username)

    def enter_password(self, password: str) -> None:
        self.password.fill(password)

    def click_login(self) -> None:
        self.login_button.click()

    def login(self, username: str, password: str) -> "SecurePage":
        """Perform full login flow and return a SecurePage instance."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        # Import here to avoid circular imports at module import time
        from pages.secure_page import SecurePage

        return SecurePage(self.page)
