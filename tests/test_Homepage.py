import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestHomepage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.driver.get("http://rahulshettyacademy.com/angularpractice/")

        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getcheckbox().click()
        self.selectOptionText(homepage.getDropdown(), getData["gender"])
        homepage.getRadioButton().click()

        homepage.getSubmit().click()
        message = homepage.getAlert().text
        log.info("message received is : "+message)
        assert "success" in message

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(
        #     ", Hello Again!!!")  # Two-way Data Binding example field
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

    # since it is used only here, we are defining in the same file instead of in conftest

    @pytest.fixture(params=HomePageData.getTestData("TC3"))
    def getData(self, request):
        return request.param
