import allure

@allure.feature('Header text')
def test_header_text(sale_page):
    sale_page.open_page()
    sale_page.check_page_header('Sale')
