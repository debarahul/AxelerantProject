import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.AddToCart import AddToCart
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.DressFlow import DressFlow


class Test_Placeorder_Flow:

    baseURL = ReadConfig.getApplicationURl()
    emailid = ReadConfig.getemailId()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_placeorder(self, setup):
        time.sleep(2)
        self.logger.info("test_placeorder")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(1)

        self.logger.info("Starting Place Order End TO End Flow")
        self.ad = AddToCart(self.driver)
        self.de = DressFlow(self.driver)
        self.de.selectEvnDress()
        self.ad.clickOnDress()
        WebDriverWait(self.driver, 10).until(ec.title_is(("Printed Dress - My Store")))
        self.ad.selectQuantity()
        self.ad.selectSize()
        self.ad.selectColor()
        self.ad.clickAddtocart()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='layer_cart_product col-xs-12 col-md-6']//h2")))
        self.ad.clickProcedToCheckoutPop()
        self.ad.clickProcedToCheckout()

        self.lg = HomePage(self.driver)
        self.lg.setEmailid(self.emailid)
        self.lg.setPassword(self.password)
        self.lg.clickSubmitLogin()
        self.logger.info("Login Successful")

        self.ad.clickProcedAdress()
        self.ad.clickCheckboxTerm()
        self.ad.clickProcedCarrier()
        self.ad.clickPaymentMethod()
        self.ad.clickConfirmOrder()
        success = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//p[@class='alert alert-success']")))
        successmsg = success.text
        if successmsg == "Your order on My Store is complete.":
            assert True
            orderdetails = self.ad.getOrderDetails()
            self.logger.info("Order Placed, Here is A Short Summary Of Order:\n{}".format(orderdetails))
            self.logger.info("Order Has Been Placed Successfully, Testcase Passed\n")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_placeorder.png")
            self.driver.close()
            self.logger.error("Order Placed Un-Successfully, Testcase Failed\n")
            assert False