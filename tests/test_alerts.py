from playwright.sync_api import Page, expect


def test_alert(page: Page):

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept())

    page.get_by_role("button", name="Click for JS Alert").click()

    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")