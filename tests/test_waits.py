from playwright.sync_api import Page, expect


def test_auto_wait(page: Page):

    page.goto("https://the-internet.herokuapp.com/login")

    username = page.get_by_role("textbox", name="Username")
    password = page.get_by_role("textbox", name="Password")
    login_button = page.get_by_role("button", name="Login")

    username.fill("tomsmith")
    password.fill("SuperSecretPassword!")

    login_button.click()

    logout_link = page.get_by_role("link", name="Logout")

    expect(logout_link).to_be_visible()