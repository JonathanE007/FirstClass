from Locators.ParisLocators import LocatorsP
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

class PageP:
    def __init__(self, driver):
        self.driver = driver
        self.login = LocatorsP.login
        self.user_login = LocatorsP.user_login
        self.password_login = LocatorsP.password_login
        self.click_login = LocatorsP.click_login
        self.search_paris = LocatorsP.search_paris
        self.enter_paris = LocatorsP.enter_paris
        self.hotels = LocatorsP.hotels
        self.restaurants = LocatorsP.restaurants
        self.activities = LocatorsP.activities
        self.paris = LocatorsP.paris
        # self.scroll_up = LocatorsP.scroll_up
        # self.scroll_down = LocatorsP.scroll_down
        self. who = LocatorsP.who
        self.trip_yoetz = LocatorsP.trip_yoetz
        self. page = LocatorsP.page
        self.about_us =LocatorsP.about_us
        self.accss = LocatorsP.accss
        self.profile = LocatorsP.profile
        self.Exit = LocatorsP.Exit

    def test_login(self):
        self.driver.find_element(By.XPATH,self.login).click()
        self.driver.find_element(By.XPATH,self.user_login).send_keys("gonathan46@gmail.com")
        self.driver.find_element(By.XPATH,self.password_login).send_keys("123456")
        self.driver.find_element(By.XPATH,self.click_login).click()
        sleep(5)
        # self.driver.implicitly_wait(10)
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        # sleep(10)

    def paris_search(self,search_paris):
        self.driver.find_element(By.XPATH, self.search_paris).send_keys(search_paris)
        self.driver.find_element(By.XPATH,self.enter_paris).send_keys(Keys.ENTER)
        # sleep(5)
        # self.driver.implicitly_wait(10)

    def paris_buttons(self):
        # self.driver.implicitly_wait(10)
        sleep(8)
        self.driver.find_element(By.XPATH,self.hotels).click()
        sleep(3)
        self.driver.find_element(By.XPATH,self.restaurants).click()
        sleep(2)
        self.driver.find_element(By.XPATH,self.activities).click()
        sleep(2)
        self.driver.find_element(By.XPATH,self.paris).click()
        # self.driver.find_element(By.XPATH,self.scroll_up).click()
        # sleep(5)
        # self.driver.find_element(By.XPATH,self.scroll_down)
        self.driver.find_element(By.XPATH,self.who).click()
        self.driver.find_element(By.XPATH,self.trip_yoetz).click()
        self.driver.find_element(By.XPATH,self.page).click()
        self.driver.find_element(By.XPATH,self.about_us).click()
        self.driver.find_element(By.XPATH,self.accss).click()
        self.driver.find_element(By.XPATH,self.profile).click()
        sleep(2)
        self.driver.find_element(By.XPATH,self.Exit).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        alert.accept()