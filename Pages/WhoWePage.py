from Locators.WhoWeLocators import LocatorsW
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class WhoWeP:
    def __init__(self,driver):
        self.driver = driver
        self.avi_git = LocatorsW.avi_git
        self.avi_linkdin = LocatorsW.avi_linkdin
        self.avi_email = LocatorsW.avi_email
        self.tikva_git = LocatorsW.tikva_git
        self.tikva_linkdin = LocatorsW.tikva_linkdin
        self.tikva_email = LocatorsW.tikva_email
        self.marcos_git = LocatorsW.marcos_git
        self.marcos_linkdin = LocatorsW.marcos_linkdin
        self.marcos_email = LocatorsW.marcos_email
        self.click_Who = LocatorsW.click_Who

    def avi_G(self):
        self.driver.find_element(By.XPATH,self.click_Who).click()
        self.driver.find_element(By.XPATH, self.avi_git).click()
        self.driver.find_element(By.XPATH, self.avi_linkdin).click()
        self.driver.find_element(By.XPATH, self.avi_email).click()

    def tikva_G(self):
        sleep(2)
        self.driver.find_element(By.XPATH,self.tikva_git).click()
        self.driver.find_element(By.XPATH,self.tikva_linkdin)
        self.driver.find_element(By.XPATH, self.tikva_email).click()

    def marcos_G(self):
        sleep(5)
        self.driver.find_element(By.XPATH, self.marcos_git).click()
        self.driver.find_element(By.XPATH, self.marcos_linkdin).click()
        self.driver.find_element(By.XPATH, self.marcos_email).click()


