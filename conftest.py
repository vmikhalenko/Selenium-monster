import pytest
from selenium import webdriver
from time import sleep
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.whats_new_page import WhatsNew


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    sleep(3)
    return chrome_driver

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
