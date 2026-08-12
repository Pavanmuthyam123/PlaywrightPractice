import json
from playwright.sync_api import Page, expect


def test_login_from_json(page: Page):

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    username = data["valid_user"]["username"]
    password = data["valid_user"]["password"]

    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )