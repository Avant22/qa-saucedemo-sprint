from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_add_to_cart_and_checkout(page_context, base_url):
    login = LoginPage(page_context)
    login.goto(base_url)
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page_context)
    inventory.add_first_item()
    expect(inventory.cart_badge).to_have_text("1")
    inventory.open_cart()
    page_context.locator('[data-test="checkout"]').click()
    page_context.locator('[data-test="firstName"]').fill("Jane")
    page_context.locator('[data-test="lastName"]').fill("Doe")
    page_context.locator('[data-test="postalCode"]').fill("12345")
    page_context.locator('[data-test="continue"]').click()
    page_context.locator('[data-test="finish"]').click()
    success = page_context.locator('[data-test="complete-header"]')
    expect(success).to_have_text("Thank you for your order!")
