import pytest
def test_adding_one_product_to_cart(product_page):
    product_page.open_page()
    product_page.adding_one_product_to_cart('1')
