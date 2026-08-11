from playwright.sync_api import sync_playwright


def test_browser_context():

    with sync_playwright() as playwright:

        # Create browser
        browser = playwright.chromium.launch(headless=False)

        # Create browser context
        context = browser.new_context()

        # Create page/tab
        page = context.new_page()

        # Open application
        page.goto("https://the-internet.herokuapp.com/login")

        # Keep browser open for observation
        page.wait_for_timeout(3000)

        # Close browser
        browser.close()