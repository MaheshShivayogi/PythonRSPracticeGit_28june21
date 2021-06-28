from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()
        homePage = HomePage(self.driver)  # Here we are passing driver from main class to HomePage class
        checkoutPage = homePage.shop()
        # We need to append self if we want to use any any elements inside method of class
        # self.driver.find_element_by_css_selector("a[href*=shop]").click()
        # Complete CSS path for getting Product Name div.card.h-100>div:nth-child(2)>h4>a
        # Complete CSS path for getting required button div.card.h-100>div>button
        # checkoutPage=CheckoutPage(self.driver)
        log.info("Getting all the product titles")
        productlst = checkoutPage.getProductTitles()
        # productlst = self.driver.find_elements_by_css_selector("div.card.h-100")
        for product in productlst:
            # productName=checkoutPage.getProductText().text
            productName = product.find_element_by_css_selector("div:nth-child(2)>h4>a").text
            if productName == "Blackberry":
                # product.checkoutPage.getProductBtn().click()
                product.find_element_by_css_selector("div>button").click()
                break
        self.driver.find_element_by_css_selector("a.nav-link.btn.btn-primary").click()
        productCheckout = self.driver.find_element_by_css_selector("h4.media-heading>a").text
        assert productName == productCheckout, "Products Mismatched"

        confirmationPage = checkoutPage.clickCheckoutItems()
        # self.driver.find_element_by_css_selector("button.btn.btn-success").click()
        log.info("Entering the Country name")
        self.driver.find_element_by_css_selector("#country").send_keys("Ind")
        # Explicit Wait
        self.verifyPresenceOfElementLocated(By.XPATH, "//a[text()='India']")
        self.driver.find_element_by_xpath("//a[text()='India']").click()
        self.driver.find_element_by_css_selector(".checkbox.checkbox-primary").click()
        # driver.find_element_by_xpath("//input[@type='checkbox']").click() #Its gives error as Element not clickable
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath("//input[@type='checkbox']")).click().perform()

        self.driver.find_element_by_css_selector("input[value=Purchase]").click()
        successmsg = self.driver.find_element_by_css_selector("div.alert.alert-success.alert-dismissible").text
        log.info("Text received from application is: "+successmsg)
        assert "Success! Thank you! Your order will be delivered in next few weeks" in successmsg, "Message mismatch"
        self.driver.get_screenshot_as_file("screen.png")
