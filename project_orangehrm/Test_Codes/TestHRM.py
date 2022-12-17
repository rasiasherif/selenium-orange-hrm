from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import Data
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
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Web Title Captured Successfully")
    
    def test_login(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=Data.HRM_Selectors.input_box_username).send_keys(Data.HRM_Data.username)
        self.driver.find_element(by=By.NAME, value=Data.HRM_Selectors.input_box_password).send_keys(Data.HRM_Data.password)
        self.driver.find_element(by=By.XPATH, value=Data.HRM_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=Data.HRM_Data.username, password=Data.HRM_Data.password))
    
    def test_invalid_login(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=Data.HRM_Selectors.input_box_username).send_keys(Data.HRM_Data.username)
        self.driver.find_element(by=By.NAME, value=Data.HRM_Selectors.input_box_password).send_keys(Data.HRM_Data.invalid_password)
        self.driver.find_element(by=By.XPATH, value=Data.HRM_Selectors.login_xpath).click()
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value=Data.HRM_Selectors.login_err_msg_xpath).text == 'Invalid credentials'
        print("FAILED # LOGIN FAILED WITH USERNAME {username} and INVALID PASSWORD {password}".format(username=Data.HRM_Data.username, password=Data.HRM_Data.invalid_password))
