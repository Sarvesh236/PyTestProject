import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.excelops import ExcelOperations


class TestHomepage(BaseClass):
    @pytest.mark.skip("Not needed")
    def test_formSubmission(self):
        file_path = "C:\\Users\\sarve\\PycharmProjects\\selfFrameworkProject\\TestData\\PythonDemo.xlsx"
        log = self.getLogger()
        homepage = HomePage(self.driver)
        exc = ExcelOperations(file_path, "Sheet1")
        rows = exc.fetch_rows()
        self.driver.get("http://rahulshettyacademy.com/angularpractice/")

        for i in range(2, rows+1):
            homepage.getName().send_keys(exc.fetch_testdata(i,2))
            homepage.getEmail().send_keys(exc.fetch_testdata(i,3))
            homepage.getPassword().send_keys(exc.fetch_testdata(i,4))
            homepage.getcheckbox().click()
            self.selectOptionText(homepage.getDropdown(), exc.fetch_testdata(i,5))
            homepage.getRadioButton().click()

            homepage.getSubmit().click()
            message = homepage.getAlert().text
            log.info("message received is : "+message)
            assert "success" in message

            homepage.getHome().click()