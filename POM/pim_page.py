from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.ProfileIcon = (By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span")
        self.LogoutOption = (By.XPATH, "//*[text()=\"Logout\"]")


    def go_to_pim(self):
        # Hover and click on PIM
        pim_element = self.driver.find_element(*self.pim_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(pim_element).click().perform()
    def Logout(self):
        self.driver.find_element(*self.ProfileIcon).click()
        self.driver.find_element(*self.LogoutOption).click()

