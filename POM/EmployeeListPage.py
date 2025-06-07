from selenium.webdriver.common.by import By
import time

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_list_menu = (By.LINK_TEXT, "Employee List")
        self.search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")

    def open_employee_list(self):
        self.driver.find_element(*self.employee_list_menu).click()

    def search_employee(self, name):
        print("serach name", name)
        self.driver.find_element(*self.search_input).click()
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(name)
        self.driver.find_element(*self.search_button).click()
        self.driver.find_element(*self.search_button).click()

        time.sleep(15)

        # Get search result name
        try:
            first = self.driver.find_element(By.XPATH, "//div[@role='table']//div[@class='oxd-table-cell oxd-padding-cell'][3]").text
            last = self.driver.find_element(By.XPATH, "//div[@role='table']//div[@class='oxd-table-cell oxd-padding-cell'][4]").text
            full_name = f"{first} {last}"
            print(f"Expected: {name}, Found: {full_name}")
            self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click()
            if name.strip().lower() == full_name.strip().lower():
                print(f"{name} Verified")
                return True
            else:
                print(f"{name} not matched in result")
                return False
        except:
            self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click()
            print(f"{name} NOT found")
            return False
