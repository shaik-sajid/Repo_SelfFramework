import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
@pytest.mark.smoke
class Test(BaseClass):
    def test_e2e(self):
        url = "https://rahulshettyacademy.com/angularpractice/"
        self.driver.get(url)
        time.sleep(2)

        home = HomePage(self.driver)
        checkout = home.shopItem()
        time.sleep(2)

        home.scrollUp()
        time.sleep(2)

        for mobile in checkout.getMobiles():
            if mobile.get_attribute("src").__contains__("blackberry.jpg"):
                checkout.getMobile().click()

        time.sleep(2)
        home.scrollDown()
        time.sleep(2)
        checkout.getCheckoutBtn1().click()
        time.sleep(2)
        confirm = checkout.getCheckoutBtn2()
        time.sleep(2)

        confirm.getDropdown().send_keys("India")
        time.sleep(8)
        confirm.getIndia().click()
        time.sleep(2)
        confirm.getCheckbox().click()
        time.sleep(2)
        confirm.getPurchase().click()
        time.sleep(2)