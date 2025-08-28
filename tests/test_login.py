from tests.pages.login_page import LoginPage

def test_login_happy_path(page_context, base_url):
    login = LoginPage(page_context)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page_context.url

def test_login_invalid_shows_error(page_context, base_url):
    login = LoginPage(page_context)
    login.login("bad_user", "bad_pass")
    assert "Epic sadface" in login.get_error_message()
