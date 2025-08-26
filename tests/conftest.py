import os
import pytest
from playwright.sync_api import Page, sync_playwright

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="session", autouse=True)
def playwright_install():
    pass

@pytest.fixture(scope="function")
def page_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def base_url():
    return BASE_URL
