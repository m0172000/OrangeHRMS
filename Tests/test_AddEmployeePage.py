import pytest

from POM.pim_page import Dashboard
from POM.add_employee_page import AddEmployeePage
from POM.EmployeeListPage import EmployeeListPage
import time

def test_add_and_verify_employees(login):
    driver=login
    # Step 1: Navigate to PIM module
    pim = Dashboard(driver)
    pim.go_to_pim()

    # Step 2: Add multiple employees
    add_page = AddEmployeePage(driver)
    employees = [("John", "Doe")]

    for first, last in employees:
        add_page.add_employee(first, last)
        time.sleep(2)  # Give time to save and redirect

    # Step 3: Go to Employee List
    emp_list = EmployeeListPage(driver)
    emp_list.open_employee_list()

    # Step 4: Verify each added employee by name
    for first, last in employees:
        full_name = f"{first} {last}"
        assert emp_list.search_employee(full_name)
