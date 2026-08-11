import json
from pathlib import Path
from playwright.sync_api import expect


def _load_data() -> dict:
    p = Path(__file__).resolve().parents[1] / "testdata" / "login_data.json"
    return json.loads(p.read_text())


def test_login_pom(login_page):
    data = _load_data()
    secure = login_page.login(data["valid"]["username"], data["valid"]["password"])

    expect(login_page.page).to_have_url(f"{login_page.base_url}/secure")
    assert "You logged into a secure area" in secure.get_flash_text()
