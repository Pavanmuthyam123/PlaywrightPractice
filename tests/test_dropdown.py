from playwright.sync_api import Page, expect


def test_dropdown(page: Page):

    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page is loaded
    dropdown = page.locator("#dropdown")
    page.wait_for_timeout(1000)  # Wait for 1 second to ensure the dropdown is loaded
    dropdown.select_option(label="Option 2")
    page.wait_for_timeout(1000)  # Wait for 1 second to ensure the selection is registered
    expect(dropdown).to_have_value("2")