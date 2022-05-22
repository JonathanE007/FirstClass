from Pages.RegisterPage import RegisterP
from Base.base import Base
from Pages.WhoWePage import WhoWeP
import pytest

@pytest.mark.usefixtures('set_up')
class Test_WhoWe(Base):

    def test_Who(self):
        driver = self.driver
        Who = WhoWeP(driver)
        Who.avi_G()
        Who.tikva_G()
        Who.marcos_G()



