import os
import pytest

@pytest.fixture(scope="function")
def app_url():
    return os.environ.get("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="function")
def page_context(page, app_url):
    page.set_default_timeout(10_000)
    page.goto(app_url)
    yield page
