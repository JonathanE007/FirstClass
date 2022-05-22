import time
from time import sleep
from Pages.RegisterPage import RegisterP
from Base.base import Base
import pytest
import requests
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures('set_up')
class TestRegister(Base):

    # @allure.description("valid")
    # @allure.severity(severity_level="critical")

    def test_register1(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        time.sleep(3)
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("123456")
        Register.enter_confirm("123456")
        Register.click_register()
    # Register without entering " first name"
    def test_register2(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("123456")
        Register.enter_confirm("123456")
        Register.click_register()

        # Register without entering "Last Name"
    # Register without entering "Last Name"
    def test_register3(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("")
        Register.birth_date('1994-06-10')
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("123456")
        Register.enter_confirm("123456")
        Register.click_register()
    # Register without entering "Date of birth"
    def test_register4(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("123456")
        Register.enter_confirm("123456")
        Register.click_register()
    # Register without entering an email
    def test_register5(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        Register.enter_email('')
        Register.enter_password("123456")
        Register.enter_confirm("123456")
        Register.click_register()
    # Register without entering password
    def test_register6(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("")
        Register.enter_confirm("123456")
        Register.click_register()
    # Register without entering confirm password
    def test_register7(self):
        driver = self.driver
        Register = RegisterP(driver)
        Register.enter_name('jonathan')
        Register.enter_last_name("elias")
        Register.birth_date('1994-06-10')
        Register.enter_email('gonathan46@gmail.com')
        Register.enter_password("123456")
        Register.enter_confirm("")
        Register.click_register()


# response = requests.get("https://trip-yoetz.herokuapp.com/login")
# print(response.status_code)
#
# print(response.json())


