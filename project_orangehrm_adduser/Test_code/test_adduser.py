from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False

class Test_OrangeHrm:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Edge()
        yield
        self.driver.close()
    
    # def test_get_title(self, booting_function):
    #     self.driver.get(self.url)
    #     assert self.driver.title == 'OrangeHRM'
    #     print("SUCCESS # Web Title Captured Successfully")
    
    def test_add_employee(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_username).send_keys(data.HRM_Data.username)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_password).send_keys(data.HRM_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.login_xpath).click()
        # click PIM from sidebar
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.pim_xpath).click()
        # click add employee button
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_add_emp_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.HRM_AddEmp_Selectors.input_box_firstName).send_keys(data.HRM_Data.firstname)
        self.driver.find_element(by=By.NAME, value=data.HRM_AddEmp_Selectors.input_box_middleName).send_keys(data.HRM_Data.middlename)
        self.driver.find_element(by=By.NAME, value=data.HRM_AddEmp_Selectors.input_box_lastName).send_keys(data.HRM_Data.lastname)
        # Save employee
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_save_emp_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print(" SUCCESS # New Employee Added ")


    def test_edit_employee(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_username).send_keys(data.HRM_Data.username)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_password).send_keys(data.HRM_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.login_xpath).click()
        # click PIM from sidebar
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.pim_xpath).click()
        # select employee
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_select_emp_xpath).click()
        # edit employee
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.input_box_DL_xpath).send_keys(data.HRM_Data.DL)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_edit_save_emp_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print(" SUCCESS # Update Employee details ")

    def test_delete_employee(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_username).send_keys(data.HRM_Data.username)
        self.driver.find_element(by=By.NAME, value=data.HRM_Selectors.input_box_password).send_keys(data.HRM_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.login_xpath).click()
        # click PIM from sidebar
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_Selectors.pim_xpath).click()
        # Delete Employee
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_delete_emp_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HRM_AddEmp_Selectors.pim_delete_confirm_emp_xpath).click()
        time.sleep(10)
        assert self.driver.title == 'OrangeHRM'
        print(" SUCCESS # Deleted  an Employee details ")

    