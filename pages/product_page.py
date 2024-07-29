from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import product_page_locators as loc

class ProductPage(BasePage):
    page_url = '/olivia-1-4-zip-light-jacket.html'

    def adding_one_product_to_cart(self,counter_number):
        size = self.find(loc.size).click()
        color = self.find(loc.color).click()
        button = self.find(loc.button).click()
        wait = WebDriverWait(self.driver, 5).until_not(EC.text_to_be_present_in_element_attribute(
                loc.counter_qty_text,
                'class',
                'empty'
            )
        )
        wait = WebDriverWait(self.driver, 5).until_not(EC.text_to_be_present_in_element_attribute(
                loc.counter_qty_text,
                'class',
                'loading'
            )
        )
        counter = self.find(loc.counter)
        assert counter.text == counter_number
