from playwright.sync_api import Page, expect


class SecurePage:
    """Page object for the Secure area after logging in."""

    def __init__(self, page: Page):
        self.page = page
        self.flash = self.page.locator("div.flash")

    def is_logged_in(self) -> bool:
        try:
            return "/secure" in self.page.url and self.flash.is_visible()
        except Exception:
            return False

    def get_flash_text(self) -> str:
        return self.flash.inner_text()

    def logout(self) -> None:
        # logout link on the page
        self.page.get_by_role("link", name="Logout").click()
