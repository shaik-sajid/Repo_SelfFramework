from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
    mobiles = (By.XPATH, "//div[@class='card h-100']/a/img")
    mobile = (By.XPATH, "(//button)[5]")
    checkoutBtn = (By.XPATH, "//*[contains(text(),'Checkout')]")

    def getMobiles(self):
        return self.driver.find_elements(*CheckoutPage.mobiles)

    def getMobile(self):
        return self.driver.find_element(*CheckoutPage.mobile)

    def getCheckoutBtn1(self):
        return self.driver.find_element(*CheckoutPage.checkoutBtn)

    def getCheckoutBtn2(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        confirm = ConfirmPage(self.driver)
        return confirm
