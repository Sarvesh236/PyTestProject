import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfiles.log')  # output file & location
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # Format
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # file handler object
        logger.setLevel(logging.DEBUG)  # levels greater than and INFO levels will be printed. Debug will not be printed
        return logger
