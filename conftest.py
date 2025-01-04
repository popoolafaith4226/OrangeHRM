import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    driver = node.funcargs.get("driver_setup")
    if driver:
        driver.save_screenshot("test_failure_screenshot.png")
