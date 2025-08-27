import os
import pytest

@pytest.fixture
def base_url(request):
    env = os.environ.get("BASE_URL")
    cli = getattr(request.config.option, "base_url", None)
    return env or cli or "https://www.saucedemo.com"

@pytest.fixture
def page_context(page, base_url):
    page.set_default_timeout(10_000)
    page.goto(base_url)
    yield page
