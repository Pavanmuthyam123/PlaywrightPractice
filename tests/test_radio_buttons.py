from playwright.sync_api import Page, expect


def test_radio_button(page: Page):

    page.goto("https://www.w3schools.com/html/html_form_input_types.asp")

    html_radio = page.locator("#html")
    css_radio = page.locator("#css")

    # Select HTML
    html_radio.check()

    # 1. Using is_checked()
    print("HTML selected:", html_radio.is_checked())

    if html_radio.is_checked():
        print("HTML radio is selected")

    # 2. Using Playwright assertion
    expect(html_radio).to_be_checked()

    # Select CSS
    css_radio.check()

    print("CSS selected:", css_radio.is_checked())

    expect(css_radio).to_be_checked()
    expect(html_radio).not_to_be_checked()