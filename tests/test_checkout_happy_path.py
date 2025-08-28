from tests.pages.login_page import LoginPage
from tests.pages.checkout_page import CheckoutPage

def test_add_to_cart_and_checkout(page_context, base_url):
    login = LoginPage(page_context)
    login.login("standard_user", "secret_sauce")

    checkout = CheckoutPage(page_context)
    checkout.add_item_to_cart("Sauce Labs Backpack")
    checkout.checkout("John", "Doe", "12345")

    assert "checkout-complete" in page_context.url
