from playwright.sync_api import Page, expect


def test_new_tab(page: Page):

    page.goto("https://the-internet.herokuapp.com/windows")

    with page.context.expect_page() as new_page_info:
        page.get_by_text("Click Here").click()

    new_page = new_page_info.value

    expect(new_page).to_have_url(
        "https://the-internet.herokuapp.com/windows/new"
    )