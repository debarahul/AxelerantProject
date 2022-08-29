import time
import logging
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="E:/Workspace/AxelerantProject/Driverdetails/chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
"""
linkList = []
elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    href = elem.get_attribute("href")
    #print(href)
    #time.sleep(2)
    if href not in linkList and href.strip():
        linkList.append(href)
print(linkList)
#print(linkList.count())
driver.quit()

mailCount, totalLinkcount, brokenlinkCount, notlinkCount, successLinkcount = 0, 0, 0, 0, 0
#linkList = ['http://automationpractice.com/index.php?controller=my-account', 'http://automationpractice.com/index.php?controller=contact', 'http://automationpractice.com/', 'http://automationpractice.com/index.php?controller=order', 'http://automationpractice.com/index.php?id_category=3&controller=category', 'http://automationpractice.com/index.php?id_category=4&controller=category', 'http://automationpractice.com/index.php?id_category=5&controller=category', 'http://automationpractice.com/index.php?id_category=7&controller=category', 'http://automationpractice.com/index.php?id_category=8&controller=category', 'http://automationpractice.com/index.php?id_category=9&controller=category', 'http://automationpractice.com/index.php?id_category=10&controller=category', 'http://automationpractice.com/index.php?id_category=11&controller=category', 'http://www.prestashop.com/?utm_source=v16_homeslider', 'http://www.prestashop.com/', 'http://automationpractice.com/index.php#homefeatured', 'http://automationpractice.com/index.php#blockbestsellers', 'http://automationpractice.com/index.php?id_product=1&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=1&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=2&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=2&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=3&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=3&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=4&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=4&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=5&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=5&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=6&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=6&token=e817bb0705dd58da8db074c69f729fd8', 'http://automationpractice.com/index.php?id_product=7&controller=product', 'http://automationpractice.com/index.php?controller=cart&add=1&id_product=7&token=e817bb0705dd58da8db074c69f729fd8', 'http://www.seleniumframework.com/', 'htdtp://www.automationpractice.com', 'https://www.facebook.com/groups/525066904174158/', 'https://twitter.com/seleniumfrmwrk', 'https://www.youtube.com/channel/UCHl59sI3SRjQ-qPcTrgt0tA', 'https://plus.google.com/111979135243110831526/posts', 'http://automationpractice.com/index.php?controller=prices-drop', 'http://automationpractice.com/index.php?controller=new-products', 'http://automationpractice.com/index.php?controller=best-sales', 'http://automationpractice.com/index.php?controller=stores', 'http://automationpractice.com/index.php?id_cms=3&controller=cms', 'http://automationpractice.com/index.php?id_cms=4&controller=cms', 'http://automationpractice.com/index.php?controller=sitemap', 'http://automationpractice.com/index.php?controller=history', 'http://automationpractice.com/index.php?controller=order-slip', 'http://automationpractice.com/index.php?controller=addresses', 'http://automationpractice.com/index.php?controller=identity', 'mailto:%73%75%70%70%6f%72%74@%73%65%6c%65%6e%69%75%6d%66%72%61%6d%65%77%6f%72%6b.%63%6f%6d']
linkList = ['hbdkgk://automationpractice.com/index.php?controller=my-account', 'hg,c://automationpractice.com/index.php?controller=contact', 'mail://automationpractice.com/', 'http://automationpractice.com/index.php?controller=order']
for link in linkList:
    if link.startswith("mail"):
        print("its is mail link")
        mailCount += 1
    elif link.startswith("http"):
        totalLinkcount += 1
        req = requests.get(link)
        if req.status_code == 200:
            print("Hello")
            successLinkcount += 1
        else:
            brokenlinkCount += 1
    else:
        print("Not a link")
        notlinkCount += 1
logging.basicConfig(filename="automation.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Total Link Count {}\nSucceed Link Count {}\nBroken Link Count {}\nMailLink Count {}\nNot a link {}".format(totalLinkcount, successLinkcount, brokenlinkCount, mailCount, notlinkCount))


class te:

    def ki(self):
        logging.basicConfig(filename="automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.CRITICAL)
        logger.debug("Harmless debug Message")
        logger.info("Just an information")
        logger.warning("Its a Warning")
        logger.error("Did you try to divide by zero")
        #logger.critical("Internet is down")

lv = te()
lv.ki()


driver = webdriver.Chrome(executable_path="E:/Workspace/AxelerantProject/Driverdetails/chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='login']")))
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(5)
driver.find_element(By.ID, "email").send_keys("axelerantpj@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("Axelerant@123")
driver.find_element(By.ID, "SubmitLogin").click()
driver.close()


act = ActionChains(driver)
woman = driver.find_element(By.XPATH, "//a[@title='Women']")
act.move_to_element(woman).perform()
dress = driver.find_element(By.LINK_TEXT, "Summer Dresses")
act.move_to_element(dress).click().perform()
sc = Select(driver.find_element(By.ID, "selectProductSort"))
sc.select_by_visible_text("Reference: Lowest first")
time.sleep(1)
driver.close()

scr = driver.find_element(By.ID, "search_query_top")
scr.clear()
scr.send_keys("dress")
driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
print("-----------------")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='lighter']")))
act = driver.title
print(act)
if act == "Search - My Store":
    print(act)
else:
    print("false")

driver.find_element(By.ID, "newsletter-input").clear()
driver.find_element(By.ID, "newsletter-input").send_keys("fglk@gmail.com")
driver.find_element(By.XPATH, "//button[@class='btn btn-default button button-small']").click()
element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//p[starts-with(@class, 'alert alert')]")))
act_message = element.text
print(act_message)
if act_message == "Newsletter : You have successfully subscribed to this newsletter.":
    print("hello")
else:
    print("No")
"""
"""
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.ID, "email").send_keys("axelerantpj@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("Axelerant@123")
driver.find_element(By.ID, "SubmitLogin").click()
time.sleep(1)
driver.find_element(By.XPATH, "//i[@class='icon-home']").click()
"""
driver.find_element(By.XPATH, "//a[@title='T-shirts']").click()
print(driver.title)

"""
driver.find_element(By.XPATH, "//a[@class='blockbestsellers']").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Best Sellers")
act = ActionChains(driver)
#WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='homefeatured']/li[5]/div/div[1]/div/a[1]")))
woman = driver.find_element(By.XPATH, "//*[@id='blockbestsellers']/li[4]/div/div[1]/div/a[1]")
act.move_to_element(woman).perform()
view = driver.find_element(By.XPATH, "//*[@id='blockbestsellers']/li[2]/div/div[2]/div[2]/a[2]")
act.move_to_element(view).click().perform()

driver.find_element(By.XPATH, "//i[@class='icon-plus']").click()
sc = Select(driver.find_element(By.ID, "group_1"))
sc.select_by_visible_text("L")
driver.find_element(By.XPATH, "//a[@name='Blue']").click()
driver.find_element(By.XPATH, "//button[@name='Submit']").click()
ele = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='layer_cart_product col-xs-12 col-md-6']//h2")))
elef = ele.text
print(elef)

gf = driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']")
gf.click()
print(driver.title)
driver.find_element(By.XPATH, "//a[@title='Proceed to checkout'][2]").click()
print(driver.title)
driver.find_element(By.XPATH, "//button[@name='processAddress']").click()
print(driver.title)
driver.find_element(By.ID, "cgv")
driver.find_element(By.XPATH, "//button[@name='processCarrier']").click()
print(driver.title)
driver.find_element(By.XPATH, "//a[@title='Pay by check.']")
print(driver.title)
#lo = driver.find_element(By.XPATH, "//p[@class='fancybox-error']")
#act.move_to_element(lo).perform()

"""







