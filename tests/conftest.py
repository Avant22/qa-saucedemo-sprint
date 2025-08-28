import os
import pytest

@pytest.fixture(scope="function")
def app_url():
    return os.environ.get("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="function")
def page_context(context, app_url, request):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.set_default_timeout(10_000)
    page.goto(app_url)
    yield page
    trace_file = os.path.join("artifacts", f"{request.node.name}-trace.zip")
    context.tracing.stop(path=trace_file)
    if request.node.rep_call.failed:
        screenshot_path = os.path.join("artifacts", f"{request.node.name}.png")
        page.screenshot(path=screenshot_path, full_page=True)
