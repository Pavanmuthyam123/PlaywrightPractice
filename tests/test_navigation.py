from playwright.sync_api import Page, expect


def test_navigation(page: Page):

    # 1. Open Login page
    page.goto("https://the-internet.herokuapp.com/login")

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )

    # 2. Login
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # 3. Verify we reached Secure Area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    # 4. Go back
    page.go_back()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )

    # 5. Go forward
    page.go_forward()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    # 6. Reload
    page.reload()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )