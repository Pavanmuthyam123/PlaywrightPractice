import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_text("tomsmith").click()
    page.get_by_text("tomsmith").click()
    page.get_by_text("tomsmith").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()