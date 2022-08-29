from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class AddToCart:
    #link_dress_xpath = "//div[@class='product-image-container']//a[@title='Printed Dress']"
    link_dress_xpath = "//a[@title='View']"
    icon_plus_xpath = "//i[@class='icon-plus']"
    drop_size_id = "group_1"
    select_color_xpath = "//a[@name='Pink']"
    link_wishlist_text = "Add to wishlist"
    size_text = "L"
    link_close_xpath = "//a[@title='Close']"
    button_homepage_xpath = "//i[@class='icon-home']"
    button_addtocart_xapth = "//button[@name='Submit']"


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

    def clickHomePage(self):
        self.driver.find_element(By.XPATH, self.button_homepage_xpath).click()

    def clickAddtocart(self):
        self.driver.find_element(By.XPATH, self.button_addtocart_xapth).click()







