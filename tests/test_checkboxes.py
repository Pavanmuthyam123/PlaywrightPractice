from playwright.sync_api import Page, expect


def test_checkbox_methods(page: Page):

    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = page.locator("input[type='checkbox']")

    # Verify number of checkboxes
    assert checkboxes.count() == 2

    # First checkbox
    first_checkbox = checkboxes.first
    first_checkbox.check()

    # Second checkbox
    last_checkbox = checkboxes.last
    last_checkbox.uncheck()

    # Check current states
    print("First:", first_checkbox.is_checked())
    print("Last:", last_checkbox.is_checked())

    # Assertions
    expect(first_checkbox).to_be_checked()
    expect(last_checkbox).not_to_be_checked()