from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    home = (By.LINK_TEXT, "Home")
    shop = (By.LINK_TEXT, "Shop")    # using Regex  XPATH - //a[contains(@href,'shop')]  CSS - a[href*='shop']
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def getHome(self):
        return self.driver.find_element(*HomePage.home)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()  # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        checkout = CheckoutPage(self.driver)
        return checkout

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.check)

    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radio)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)

