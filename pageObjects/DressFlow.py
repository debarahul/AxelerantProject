from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DressFlow:
    link_woman_text = "//a[@title='Women']"
    link_sumdress_text = "Summer Dresses"
    link_evndress_text = "Evening Dresses"

    def __init__(self,driver):
        self.driver = driver

    def selectSumDress(self):
        act = ActionChains(self.driver)
        woman = self.driver.find_element(By.XPATH, self.link_woman_text)
        act.move_to_element(woman).perform()
        dress = self.driver.find_element(By.LINK_TEXT, self.link_sumdress_text)
        act.move_to_element(dress).click().perform()


    def selectEvnDress(self):
        act = ActionChains(self.driver)
        woman = self.driver.find_element(By.XPATH, self.link_woman_text)
        act.move_to_element(woman).perform()
        dress = self.driver.find_element(By.LINK_TEXT, self.link_evndress_text)
        act.move_to_element(dress).click().perform()

    