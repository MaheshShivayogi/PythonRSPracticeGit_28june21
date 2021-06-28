import pytest
from pageObjects.HomePage import HomePage
from testData.HomePageTestData import HomePageTestData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log=self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First Name is: "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        log.info("Email is: " + getData["email"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getCheckMeOut().click()
        log.info("Gender is: " + getData["gender"])
        self.selectOptionsByVisibleText(homePage.getGenderDDL(),getData["gender"])
        homePage.getSubmitBtn().click()
        print(homePage.getAlertSuccessMsg().text)
        msgSuccess = homePage.getAlertSuccessMsg().text
        assert "success" in msgSuccess

    @pytest.fixture(params=HomePageTestData.getTestData("t3"))
    def getData(self, request):
        return request.param





