import time
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.HomePage import HomePage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen

class Test_home_page:

    baseURL = ReadConfig.getApplicationURl()
    emailid = ReadConfig.getemailId()
    password = ReadConfig.getPassword()
    subemailid = ReadConfig.getsubemail()
    searchvalue = ReadConfig.getsearchvalue()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_baseurl(self,setup):
        time.sleep(3)
        self.logger.info("test_baseurl")
        self.logger.info("Verify Base Url")
        self.driver = setup
        self.driver.get(self.baseURL)
        url = self.driver.current_url
        if url == self.baseURL:
            assert True
            self.driver.close()
            self.logger.info("Test BaseUrl Testcase Is Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_baseurl.png")
            self.driver.close()
            self.logger.error("Test BaseUrl Testcase Is Failed")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        time.sleep(3)
        self.logger.info("test_homePageTitle")
        self.logger.info("Verify Home Page Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "My Store":
            assert True
            self.driver.close()
            self.logger.info("Home Page Title Testcase Is Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Home Page Title Testcase Is Failed")
            assert False


    @pytest.mark.regression
    def test_searchbar(self, setup):
        time.sleep(3)
        self.logger.info("test_searchbar")
        self.logger.info("Verify The Searchbar")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sb = HomePage(self.driver)
        self.sb.setSearchbarText(self.searchvalue)
        self.sb.clickSearch()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='lighter']")))
        act_title = self.driver.title
        if act_title == "Search - My Store":
            assert True
            self.driver.close()
            self.logger.info("Searchbar Working, Testcase Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchbar.png")
            self.driver.close()
            self.logger.error("Searchbar Not Working, Testcase Failed")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        time.sleep(3)
        self.logger.info("test_login")
        self.logger.info("Verify The Login Flow")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='login']")))
        self.lg.clickSignin()
        WebDriverWait(self.driver, 10).until(ec.title_is("Login - My Store"))
        self.lg.setEmailid(self.emailid)
        self.lg.setPassword(self.password)
        self.lg.clickSubmitLogin()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "My account - My Store":
            assert True
            self.driver.close()
            self.logger.info("Login Successfully, Testcase Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("Login Un-Successfully, Testcase Failed")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self,setup):
        time.sleep(3)
        self.logger.info("test_logout")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = HomePage(self.driver)
        self.lg.clickSignin()
        WebDriverWait(self.driver, 10).until(ec.title_is("Login - My Store"))
        self.lg.setEmailid(self.emailid)
        self.lg.setPassword(self.password)
        self.lg.clickSubmitLogin()
        self.logger.info("Login Successful")

        self.logger.info("Started The Logout Flow")
        self.lg.clickSignout()
        act_title = self.driver.title
        if act_title == "Login - My Store":
            assert True
            self.driver.close()
            self.logger.info("Logout Successfully, Testcase Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout.png")
            self.driver.close()
            self.logger.error("Logout Un-Successfully, Testcase Failed")
            assert False


    @pytest.mark.regression
    def test_newsletter(self,setup):
        time.sleep(3)
        self.logger.info("test_newsletter")
        self.logger.info("Verify Newsletter Functionality")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.nl = HomePage(self.driver)
        self.nl.setSubscribedEmail(self.subemailid)
        self.nl.clickForSubsc()
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//p[starts-with(@class, 'alert alert')]")))
        act_message = element.text
        if act_message == "Newsletter : You have successfully subscribed to this newsletter.":
            assert True
            self.driver.close()
            self.logger.info("Newsletter Successfully Subscribed For {}, Testcase Passed".format(self.subemailid))
        elif act_message == "Newsletter : This email address is already registered.":
            assert True
            self.driver.close()
            self.logger.info("Already Registered For Newsletter And Email is {}, Testcase Passed".format(self.subemailid))
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsletter.png")
            self.driver.close()
            self.logger.error("Newsletter Registered Un-Successful, Testcase Failed")
            assert False

    """
    @pytest.mark.regression
    def test_link(self,setup):
        time.sleep(3)
        self.logger.info("test_link")
        self.logger.info("Verify All Details In Home Page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lk = HomePage(self.driver)
        maillinkCount, brokenlinkCount, notlinkCount, successLinkcount = 0, 0, 0, 0
        try:
            for link in self.lk.getAllLink():
                if link.startswith("mail"):
                    maillinkCount += 1
                elif link.startswith("http"):
                    req = requests.get(link)
                    if req.status_code == 200:
                        successLinkcount += 1
                    else:
                        brokenlinkCount += 1
                else:
                    notlinkCount += 1

            self.logger.info("All link Details\nSucceed Link Count {}\nBroken Link Count {}\nMailLink Count {}\nNot a link {}".format(successLinkcount, brokenlinkCount, maillinkCount, notlinkCount))
            assert True
            self.logger.info("Completed All Link Details")

        except:
            self.logger.error("There Are Some Error While Validate The Links")
            assert False         
    """

    










