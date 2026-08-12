from playwright.sync_api import Page, expect


def test_buttons_and_links(page: Page):

    # 1. Open login page
    page.goto("https://the-internet.herokuapp.com/login")

    # 2. Locate Login button using get_by_role()
    login_button = page.get_by_role("button", name="Login")

    # 3. Verify Login button is visible
    expect(login_button).to_be_visible()

    # 4. Verify Login button is enabled
    expect(login_button).to_be_enabled()

    # 5. Fill valid credentials
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")

    # 6. Click Login
    login_button.click()

    # 7. Verify /secure
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    # 8. Locate Logout link
    logout_link = page.get_by_role("link", name="Logout")

    # 9. Click Logout
    logout_link.click()

    # 10. Verify /login
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )