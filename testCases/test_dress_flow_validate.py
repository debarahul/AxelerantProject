import time
import pytest
from pageObjects.DressFlow import DressFlow
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen


class Test_dress_flow:
    baseURL = ReadConfig.getApplicationURl()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_summer_dress(self,setup):
        time.sleep(3)
        self.logger.info("test_dressflow")
        self.logger.info("Verify The Dress Flow")
        self.driver = setup
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.baseURL)
        self.df = DressFlow(self.driver)
        self.df.selectSumDress()
        act_title = self.driver.title
        if act_title == "Summer Dresses - My Store":
            assert True
            self.driver.close()
            self.logger.info("Successes Landed To Summer Dresses Page, Testcase Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_dressflow.png")
            self.driver.close()
            self.logger.error("Page Title Is Different, Testcase Failed")
            assert False



