import pathlib
import pytest
from playwright.sync_api import Page

from config.config import BASE_URL
from pages.login_page import LoginPage
from utilities.logger import get_logger


@pytest.fixture(scope="session")
def base_url() -> str:
    """Return the base URL for the AUT from config."""
    return BASE_URL


@pytest.fixture
def logger():
    return get_logger("tests")


@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    """Return a `LoginPage` instance already navigated to the login URL."""
    lp = LoginPage(page, base_url)
    lp.navigate()
    return lp