from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = lambda item_name: page.locator(f"text={item_name}")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.zip_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

    def add_item_to_cart(self, item_name: str):
        self.add_to_cart_button(item_name).click()
        self.cart_icon.click()

    def checkout(self, first_name: str, last_name: str, zip_code: str):
        self.checkout_button.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_input.fill(zip_code)
        self.continue_button.click()
        self.finish_button.click()
