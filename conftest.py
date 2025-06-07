import os
from datetime import datetime

import pytest
from selenium import webdriver

from POM.login_pages import LoginPage
from POM.logout import LogoutPage


@pytest.fixture()
def setup():
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def login(setup):
    driver=setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    yield driver
    # Logout from the application
    logout = LogoutPage(driver)
    logout.logout()
    assert "login" in driver.current_url.lower()

