from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage

def test_login_happy_path(page_context, base_url):
    login = LoginPage(page_context)
    login.goto(base_url)
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page_context)
    assert inventory.title.inner_text().strip().lower() == "products"

def test_login_invalid_shows_error(page_context, base_url):
    login = LoginPage(page_context)
    login.goto(base_url)
    login.login("invalid_user", "wrong")
    assert login.error.is_visible()
