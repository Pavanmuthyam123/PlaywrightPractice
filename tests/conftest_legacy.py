import pytest
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page):

    # SETUP
    print("\n--- SETUP: Opening Login Page ---")

    page.goto("https://the-internet.herokuapp.com/login")

    # Give page to test
    yield page

    # TEARDOWN
    print("\n--- TEARDOWN: Test Completed ---")
