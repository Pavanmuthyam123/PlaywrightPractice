from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(f"{self.base_url}/login")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()