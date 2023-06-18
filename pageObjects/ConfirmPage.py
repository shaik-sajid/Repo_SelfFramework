from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
    selectDropdown = (By.XPATH, "//input[@id='country']")
    selectIndia = (By.XPATH, "//a[contains(text(),'India')]")
    checkBox = (By.XPATH, "//label[@for='checkbox2']")
    purchaseBtn = (By.XPATH, "//input[@value='Purchase']")

    def getDropdown(self):
        return self.driver.find_element(*ConfirmPage.selectDropdown)

    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.selectIndia)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)