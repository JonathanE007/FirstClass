import time
from Locators.RegisterLocators import LocatorsR
from selenium.webdriver.common.by import By

class RegisterP:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = LocatorsR.first_name
        self.last_name = LocatorsR.last_name
        self.email = LocatorsR.email
        self.date = LocatorsR.date
        self.password = LocatorsR.password
        self.confirm = LocatorsR.confirm
        self.send = LocatorsR.send

    def enter_name(self,first_name):
        # self.driver.find_element(By.XPATH, self.first_name).clear()
        self.driver.find_element(By.XPATH, self.first_name).send_keys(first_name)
        time.sleep(3)

    def enter_last_name(self,last_name):
        # self.driver.find_element_by_name(self.last_name).clear()
        self.driver.find_element(By.XPATH,self.last_name).send_keys(last_name)

    def enter_email(self,email):
        # self.driver.find_element_by_name(self.email).clear()
        self.driver.find_element(By.XPATH,self.email).send_keys(email)

    def birth_date(self, date):
        self.driver.execute_script(f"document.getElementsByClassName('register-input')[2].value = '{date}'")

    def enter_password(self,password):
        # self.driver.find_element_by_name(self.password).clear()
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    def enter_confirm(self,confirm ):
        # self.driver.find_element_by_name(self.confirm).clear()
        self.driver.find_element(By.XPATH,self.confirm).send_keys(confirm)

    def click_register(self):
        self.driver.find_element(By.XPATH,self.send).click()

