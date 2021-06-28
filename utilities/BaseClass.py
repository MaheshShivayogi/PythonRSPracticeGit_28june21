import inspect
import logging
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def verifyPresenceOfElementLocated(self, locator, webElement):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((locator, webElement)))

    def selectOptionsByVisibleText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

