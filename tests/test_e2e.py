from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.driver.get("http://rahulshettyacademy.com/angularpractice/")
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        products = checkoutpage.getCardTitles()
        for p in products:
            productName = p.find_element(By.CSS_SELECTOR, "h4 a").text
            log.info(productName)
            if productName == "Blackberry":
                p.find_element(By.CSS_SELECTOR, "div div button").click()

        checkoutpage.getCheckoutButton().click()
        confirmpage = checkoutpage.getCheckoutSuccess()
        log.info("Entering country name as ind")
        confirmpage.searchKeys().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.selectCountry().click()
        confirmpage.checkBox().click()
        confirmpage.submitButton().click()
        message = confirmpage.successMessage().text
        log.info("Text received from app is: "+message)
        assert "Success! Thank you!" in message
        # assert "Success! asfjklanfjsaThank you!" in message ---> deliberately failing to check screenshot function
