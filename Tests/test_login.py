from POM.login_pages import LoginPage
from selenium import webdriver


def test_valid_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login=LoginPage(driver)
    login.login("Admin","admin123")
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in driver.current_url