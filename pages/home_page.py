from pages.base_page import BasePage
from pages.locators import drop_menu_locators as loc
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    page_url = '/'
    def drop_menu(self,text):
        women = self.find(loc.women)
        tops = self.find(loc.tops)
        jackets = self.find(loc.jackets)
        actions = ActionChains(self.driver).move_to_element(women).move_to_element(tops).click(jackets)
        actions.perform()
        jackets_header = self.find(loc.jackets_header)
        assert jackets_header.text == text
