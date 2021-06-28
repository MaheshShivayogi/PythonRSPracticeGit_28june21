from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        # driver of main class (test_e2e) is assigned to local class driver(self.driver)
        self.driver = driver

    lnkShop = (By.CSS_SELECTOR, "a[href*=shop]")  # tupple which will accept 2 arguments. Which locator and path

    # self.driver.find_element_by_name("name")
    txtName = (By.NAME, "name")

    # self.driver.find_element_by_css_selector("input[name=email]")
    txtEmail = (By.CSS_SELECTOR, "input[name=email]")

    # self.driver.find_element_by_id("exampleCheck1")
    chkCheckMeOut = (By.ID, "exampleCheck1")

    # self.driver.find_element_by_xpath("//input[@value='Submit']")
    btnSubmit = (By.XPATH, "//input[@value='Submit']")

    # self.driver.find_element_by_class_name("alert-success")
    msgAlertSuccess = (By.CLASS_NAME, "alert-success")

    # self.driver.find_element_by_id("exampleFormControlSelect1")
    ddlGender = (By.ID, "exampleFormControlSelect1")

    def shop(self):
        self.driver.find_element(*HomePage.lnkShop).click()# Similar to driver.find_element_by_css_selector("a[href*=shop]")
        # driver should come from main class where TC exists. Inorder to we need to create parameterized constructor and pass driver as an argument
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.txtName)

    def getEmail(self):
        return self.driver.find_element(*HomePage.txtEmail)

    def getCheckMeOut(self):
        return self.driver.find_element(*HomePage.chkCheckMeOut)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.btnSubmit)

    def getAlertSuccessMsg(self):
        return self.driver.find_element(*HomePage.msgAlertSuccess)

    def getGenderDDL(self):
        return self.driver.find_element(*HomePage.ddlGender)