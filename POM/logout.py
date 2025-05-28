from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.LINK_TEXT, "Logout")

    def logout(self):
        self.driver.find_element(*self.profile_icon).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_button).click()
