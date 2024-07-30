from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import login_locators as loc
import allure


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'

    @allure.step('Enter email, password and click the button')
    def fill_login_form(self,login,password):
        email_field = self.find(loc.email_locator)
        password_field = self.find(loc.password_locator)
        button = self.find(loc.button_locator)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    @allure.step('Check message')
    def check_error_alert_text(self,text):
        error_alert_location = (WebDriverWait(self.driver, 5).until(EC.presence_of_element_located
            (loc.error_alert_locator)
        )
        )
        assert error_alert_location.text == text