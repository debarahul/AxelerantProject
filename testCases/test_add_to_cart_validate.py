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


class Test_Addtocart_flow:

    baseURL = ReadConfig.getApplicationURl()
    emailid = ReadConfig.getemailId()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addtoWishlist(self,setup):
        time.sleep(3)
        self.logger.info("test_addtocart")
        self.logger.info("Verify Add To Cart Flow")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(0.5)

        self.ad = AddToCart(self.driver)
        self.de = DressFlow(self.driver)
        self.de.selectEvnDress()

        self.ad.clickOnDress()
        WebDriverWait(self.driver, 10).until(ec.title_is(("Printed Dress - My Store")))
        self.ad.selectQuantity()
        self.ad.selectSize()
        self.ad.selectColor()
        self.ad.selectWishlist()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//p[@class='fancybox-error']")))
        act_text = self.driver.find_element(By.XPATH, "//p[@class='fancybox-error']").text
        if act_text == "You must be logged in to manage your wishlist.":
            self.ad.clickClose()
            assert True
            self.driver.close()
            self.logger.info("{}, Testcase Passed".format(act_text))
        elif act_text == "Added to your wishlist.":
            assert True
            self.driver.close()
            self.logger.info("{}, Testcase Passed".format(act_text))
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addtoWishlist.png")
            self.driver.close()
            self.logger.error("Item added to wishlist unsuccessfully, Testcase Failed")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addtocart(self,setup):
        time.sleep(3)
        self.logger.info("test_addtocart")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(1)
        #self.driver.maximize_window()

        self.lg = HomePage(self.driver)
        self.lg.clickSignin()
        WebDriverWait(self.driver, 10).until(ec.title_is("Login - My Store"))
        self.lg.setEmailid(self.emailid)
        self.lg.setPassword(self.password)
        self.lg.clickSubmitLogin()
        self.logger.info("Login Successful")


        self.logger.info("Starting Add To Cart Flow")
        self.ad = AddToCart(self.driver)
        self.de = DressFlow(self.driver)
        self.de.selectEvnDress()

        self.ad.clickOnDress()
        WebDriverWait(self.driver, 10).until(ec.title_is(("Printed Dress - My Store")))
        self.ad.selectQuantity()
        self.ad.selectSize()
        self.ad.selectColor()
        self.ad.clickAddtocart()
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='layer_cart_product col-xs-12 col-md-6']//h2")))
        element = element.text
        if element == "Product successfully added to your shopping cart":
            assert True
            self.driver.close()
            self.logger.info("{}, Testcase Passed".format(element))
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addtocart.png")
            self.driver.close()
            self.logger.error("Item added to cart unsuccessfully, Testcase Failed")
            assert False



