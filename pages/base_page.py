from selenium.webdriver.remote.webdriver import WebDriver
import allure

class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the page')
    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened by URL for this page')

    @allure.step('Find element by locator')
    def find(self,locator:tuple):
        return self.driver.find_element(*locator)


