from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector("div.card.h-100")
    lstProducts = (By.CSS_SELECTOR, "div.card.h-100")

    # find_element_by_css_selector("div:nth-child(2)>h4>a")
    txtProduct = (By.CSS_SELECTOR, "div:nth-child(2)>h4>a")

    # find_element_by_css_selector("div>button")
    btnProduct = (By.CSS_SELECTOR, "div>button")

    # driver.find_element_by_css_selector("button.btn.btn-success")
    btnCheckout = (By.CSS_SELECTOR, "button.btn.btn-success")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.lstProducts)

    def getProductText(self):
        return self.driver.find_element(*CheckoutPage.txtProduct)

    def getProductBtn(self):
        return self.driver.find_element(*CheckoutPage.btnProduct)

    def clickCheckoutItems(self):
        self.driver.find_element(*CheckoutPage.btnCheckout).click()
        confirmationPage=ConfirmationPage(self.driver)
        return confirmationPage
