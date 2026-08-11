import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def login_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    return page


def test_login_page(login_page: Page):

    expect(login_page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )