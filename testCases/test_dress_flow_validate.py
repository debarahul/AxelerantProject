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


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_sorting(self,setup):
        time.sleep(3)
        self.logger.info("test_sorting")
        self.driver = setup
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.baseURL)
        self.driver.get(self.baseURL)
        self.df = DressFlow(self.driver)
        self.df.selectSumDress()
        self.logger.info("Successfully Landed On Summer Dress Listing Page")

        self.logger.info("Verify The Sorting")
        beforelist = self.df.getPriceList()
        self.df.setSorting()
        time.sleep(8)
        afterlist = self.df.getPriceList()
        beforelist.sort(reverse=True)

        self.logger.info("Compare Before And After Sorting Result")
        if beforelist == afterlist:
            assert True
            self.driver.close()
            self.logger.info("Sorting is successful, Testcase Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_sorting.png")
            self.driver.close()
            self.logger.error("Sorting doesn't work, Testcase Failed")
            assert False




