from Base.base import Base
from Pages.ParisPage import PageP
import pytest

@pytest.mark.usefixtures('set_up')
class TestP(Base):

    def test_paris(self):
        driver = self.driver
        paris = PageP(driver)
        paris.test_login()
        paris.paris_search("paris")
        paris.paris_buttons()

