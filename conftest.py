import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.whats_new_page import WhatsNew
import allure

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_argument('--disable-infobars')
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver = webdriver.Chrome()

    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    sleep(3)
    yield chrome_driver
    allure.attach(chrome_driver.get_screenshot_as_png())

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture()
def home_page(driver):
    return HomePage(driver)

@pytest.fixture()
def whats_new_page(driver):
    return WhatsNew(driver)
