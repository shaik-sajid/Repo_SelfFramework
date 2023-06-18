from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    shop = (By.XPATH, "//a[contains(text(),'Shop')]")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        confirm = CheckoutPage(self.driver)
        return confirm

    def scrollUp(self):
        self.driver.execute_script("window.scrollBy(0, 500)")

    def scrollDown(self):
        self.driver.execute_script("window.scrollBy(0, -500)")