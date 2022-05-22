from selenium import webdriver
import pytest

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome("C:/Users/97252/PycharmProjects/Chrome/driver/chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://trip-yoetz.herokuapp.com/register")
        self.driver.maximize_window()
        yield self.driver
        print("Tests is finished")
        self.driver.close()
        self.driver.quit()

