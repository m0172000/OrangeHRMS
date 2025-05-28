from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.Driver = driver
        self.Username_input = (By.NAME, "username")
        self.Password_input = (By.NAME, "password")
        self.Login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.Driver.find_element(*self.Username_input).send_keys(username)
        self.Driver.find_element(*self.Password_input).send_keys(password)
        self.Driver.find_element(*self.Login_button).click()
