from selenium.webdriver.common.by import By


class HomePage:
    link_signin_text = "Sign in"
    textbox_email_id = "email"
    textbox_password_id = "passwd"
    button_submit_id = "SubmitLogin"
    link_xpath = "//a[@href]"
    textbox_searchbar_id = "search_query_top"
    button_search_xpath = "//button[@name='submit_search']"
    textbox_newsletter_id = "newsletter-input"
    button_newsletter_xpath = "//button[@class='btn btn-default button button-small']"
    link_signout_xpath = "//a[@class='logout']"



    def __init__(self,driver):
        self.driver = driver

    def setSearchbarText(self, searchvalue):
        searchbar = self.driver.find_element(By.ID, self.textbox_searchbar_id)
        searchbar.clear()
        searchbar.send_keys(searchvalue)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def clickSignin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_signin_text).click()

    def setEmailid(self, emailid):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(emailid)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickSubmitLogin(self):
        self.driver.find_element(By.ID, self.button_submit_id).click()

    def getAllLink(self):
        linkList = []
        elems = self.driver.find_elements(By.XPATH, self.link_xpath)
        for elem in elems:
            href = elem.get_attribute("href")
            if href not in linkList and href.strip():
                linkList.append(href)
        self.driver.close()
        return linkList

    def setSubscribedEmail(self, subemailid):
        self.driver.find_element(By.ID, self.textbox_newsletter_id).clear()
        self.driver.find_element(By.ID, self.textbox_newsletter_id).send_keys(subemailid)

    def clickForSubsc(self):
        self.driver.find_element(By.XPATH, self.button_newsletter_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.link_signout_xpath).click()








