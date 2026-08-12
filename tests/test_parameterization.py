import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize(
    "username,password",
    [
        ("tomsmith", "SuperSecretPassword!"),
        ("wronguser", "wrongpassword"),
    ]
)
def test_login_data(page: Page, username, password):

    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)

    page.get_by_role("button", name="Login").click()