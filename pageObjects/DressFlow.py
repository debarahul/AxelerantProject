from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class DressFlow:
    link_woman_text = "//a[@title='Women']"
    link_sumdress_text = "Summer Dresses"
    link_evndress_text = "Evening Dresses"
    link_pricelist_xpath = "//span[@class='price product-price']"
    button_dropdown_id = "selectProductSort"
    dropdown_text = "Price: Highest first"
    checkbox_instock_xpath = "//input[@name='layered_quantity_1']"
    value_instock_xpath = "//span[@class='available-now']"
    alert_noproduct_xpath = "//p[contains(@class,'warning')]"

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

    def getPriceList(self):
        listing = self.driver.find_elements(By.XPATH, self.link_pricelist_xpath)
        pricelist = []
        for i in listing:
            j = i.text
            if j != '':
                pricelist.append(float(j.replace("$", "")))
        return pricelist

    def setSorting(self):
        scsort = Select(self.driver.find_element(By.ID, self.button_dropdown_id))
        scsort.select_by_visible_text(self.dropdown_text)

    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkbox_instock_xpath).click()

    def getInstockList(self):
        lists = self.driver.find_elements(By.XPATH, self.value_instock_xpath)
        instocklist = []
        for i in lists:
            j = i.text
            instocklist.append(j)
        return instocklist

    def getAlertMsg(self):
        message = self.driver.find_element(By.XPATH,  self.alert_noproduct_xpath).text
        return message
