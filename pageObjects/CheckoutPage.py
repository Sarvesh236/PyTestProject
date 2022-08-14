from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, "app-card-list app-card")
    checkoutbutton = (By.CSS_SELECTOR, ".btn-primary")
    checkoutsuccess = (By.CSS_SELECTOR, ".btn-success")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton)

    def getCheckoutSuccess(self):
        self.driver.find_element(*CheckoutPage.checkoutsuccess).click()
        confirm = ConfirmationPage(self.driver)
        return confirm


