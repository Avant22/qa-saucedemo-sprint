import os
import pytest

@pytest.fixture(scope="function")
def base_url():
    return os.environ.get("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="function")
def page_context(page, base_url):
    page.set_default_timeout(10_000)
    page.goto(base_url)
    yield page
