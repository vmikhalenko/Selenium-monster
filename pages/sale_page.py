from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header(self,text):
        header_text = self.find(loc.header_text_locator)
        assert header_text.text == text