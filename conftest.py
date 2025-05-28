import os
from datetime import datetime

import pytest
from selenium import webdriver

from POM.login_pages import LoginPage
from POM.logout import LogoutPage


@pytest.fixture()
def driver():
    #Set up WebDriver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    yield driver
    ## Logout from The application
    logout = LogoutPage(driver)
    logout.logout()
    assert "login" in driver.current_url.lower()
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test failure (call phase)
    if report.when == "call" and report.failed:
        # Try to get driver from fixtures (either 'driver' or 'login')
        driver = item.funcargs.get("driver") or item.funcargs.get("login")
        if driver:
            # Create screenshots folder if not exists
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            # Format filename
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_").replace("\\", "_")
            filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"

            # Take screenshot
            driver.save_screenshot(filename)
            print(f"\n🖼️ Screenshot saved to: {filename}")