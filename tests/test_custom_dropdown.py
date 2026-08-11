from playwright.sync_api import Page, expect


def test_custom_dropdown(page: Page):

    page.goto("https://the-internet.herokuapp.com/jqueryui/menu")

    # 1. Click Enabled
    page.get_by_text("Enabled", exact=True).hover()

    # 2. Hover Downloads
    page.get_by_text("Downloads", exact=True).hover()

    # 3. Click Excel
    page.get_by_text("Excel", exact=True).click()