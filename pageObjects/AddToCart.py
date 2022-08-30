from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class AddToCart:

    link_dress_xpath = "//a[@title='View']"
    icon_plus_xpath = "//i[@class='icon-plus']"
    drop_size_id = "group_1"
    select_color_xpath = "//a[@name='Pink']"
    link_wishlist_text = "Add to wishlist"
    size_text = "L"
    link_close_xpath = "//a[@title='Close']"
    button_homepage_xpath = "//i[@class='icon-home']"
    button_addtocart_xapth = "//button[@name='Submit']"
    link_procedTo_xpath = "//a[@title='Proceed to checkout']"
    button_procedToCheck_xpath = "//p[@class='cart_navigation clearfix']//a[contains(@title,'checkout')]"
    button_procedAdress_xpath = "//button[@name='processAddress']"
    button_procedCarrier_xpath = "//button[@name='processCarrier']"
    check_termOfService_id = "cgv"
    option_payment_class = "cheque"
    button_confirmOrder_xpath = "//button[contains(@class,'button-medium')]"
    value_orderdetails_xpath = "//div[contains(@class,'order-confirmation')]"



    def __init__(self,driver):
        self.driver = driver


    def clickOnDress(self):
        self.driver.find_element(By.XPATH, self.link_dress_xpath).click()


    def selectQuantity(self):
        self.driver.find_element(By.XPATH, self.icon_plus_xpath).click()

    def selectSize(self):
        size = Select(self.driver.find_element(By.ID, self.drop_size_id))
        size.select_by_visible_text(self.size_text)

    def selectColor(self):
        self.driver.find_element(By.XPATH, self.select_color_xpath).click()

    def selectWishlist(self):
        self.driver.find_element(By.LINK_TEXT, self.link_wishlist_text).click()

    def clickClose(self):
        act = ActionChains(self.driver)
        cls = self.driver.find_element(By.XPATH, self.link_close_xpath)
        act.move_to_element(cls).click().perform()

    def clickAddtocart(self):
        self.driver.find_element(By.XPATH, self.button_addtocart_xapth).click()


    def clickProcedToCheckoutPop(self):
        self.driver.find_element(By.XPATH, self.link_procedTo_xpath).click()

    def clickProcedToCheckout(self):
        self.driver.find_element(By.XPATH, self.button_procedToCheck_xpath).click()

    def clickProcedAdress(self):
        self.driver.find_element(By.XPATH, self.button_procedAdress_xpath).click()

    def clickProcedCarrier(self):
        self.driver.find_element(By.XPATH, self.button_procedCarrier_xpath).click()

    def clickCheckboxTerm(self):
        self.driver.find_element(By.ID, self.check_termOfService_id).click()

    def clickPaymentMethod(self):
        self.driver.find_element(By.CLASS_NAME, self.option_payment_class).click()

    def clickConfirmOrder(self):
        self.driver.find_element(By.XPATH, self.button_confirmOrder_xpath).click()

    def getOrderDetails(self):
        details = self.driver.find_element(By.XPATH, self.value_orderdetails_xpath)
        return details.text






