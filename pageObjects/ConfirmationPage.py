from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR, "#country")
    selectcountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def searchKeys(self):
        return self.driver.find_element(*ConfirmationPage.search)

    # def explicitWait(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     return wait.until(expected_conditions.presence_of_element_located(*ConfirmationPage.selectcountry))

    def selectCountry(self):
        return self.driver.find_element(*ConfirmationPage.selectcountry)

    def checkBox(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)

    def submitButton(self):
        return self.driver.find_element(*ConfirmationPage.submit)

    def successMessage(self):
        return self.driver.find_element(*ConfirmationPage.success)



