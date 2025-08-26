from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_add_btn = page.locator('button[data-test^="add-to-cart"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.menu_btn = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_first_item(self):
        self.first_add_btn.first.click()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_btn.click()
        self.logout_link.click()
