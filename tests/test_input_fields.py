from playwright.sync_api import Page, expect


def test_keyboard_tab(page: Page):

    page.goto("https://the-internet.herokuapp.com/login")

    username = page.locator("#username")
    password = page.locator("#password")

    username.fill("tomsmith")

    username.press("Tab")

    password.fill("SuperSecretPassword!")

    expect(username).to_have_value("tomsmith")
    expect(password).to_have_value("SuperSecretPassword!")