def test_navigation_pom(page, base_url):

    # 1. Open login page
    page.goto(f"{base_url}/login")
    assert page.url.endswith("/login")

    # 2. Navigate to a public page
    page.goto(f"{base_url}/checkboxes")
    assert page.url.endswith("/checkboxes")

    # 3. Go back
    page.go_back()
    assert page.url.endswith("/login")

    # 4. Go forward
    page.go_forward()
    assert page.url.endswith("/checkboxes")