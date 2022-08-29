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
    def test_sorting_result(self,setup):
        self.logger.info("test_sorting_result")
        self.driver = setup
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.baseURL)
        self.driver.get(self.baseURL)
        self.df = DressFlow(self.driver)
        self.df.selectSumDress()
        self.logger.info("Successfully Landed On Summer Dress Listing Page")

        self.logger.info("Verify The Sorting Result")
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


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_checkbox_result(self,setup):
        self.logger.info("test_checkbox_result")
        self.driver = setup
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.baseURL)
        self.driver.get(self.baseURL)
        self.df = DressFlow(self.driver)
        self.df.selectSumDress()
        self.logger.info("Successfully Landed On Summer Dress Listing Page")

        self.logger.info("Verify The Checkbox Result")
        beforecheck = self.df.getInstockList()
        self.logger.info("The Check Box Test Is Based On Value {}".format(beforecheck[1]))

        self.df.clickCheckBox()
        time.sleep(5)
        msg = self.df.getAlertMsg()
        if msg == "There are no products.":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkbox_result.png")
            self.driver.close()
            self.logger.error("After Checkbox Select There Are No Product, Testcase Failed")
            assert False
        else:
            aftercheck = self.df.getInstockList()
            if beforecheck == aftercheck:
                assert True
                self.driver.close()
                self.logger.info("After Checkbox There Are Expected Result Coming, Testcase Passed")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_checkbox_result.png")
                self.driver.close()
                self.logger.error("After Checkbox Select There Are Different List, Testcase Failed")
                assert False





