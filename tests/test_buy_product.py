import allure

from selenium import webdriver

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.whisky_page import WhiskyPage

@allure.description("Test buying 1 product")
def test_buy_product_1(set_up, set_group):
    # Sanity test: buying 1 product with giftbox using sorting by price
    driver = webdriver.Chrome()

    mp = MainPage(driver)
    mp.go_to_whisky_page()

    wp = WhiskyPage(driver)
    wp.add_to_cart_product_1()

    cp = CartPage(driver)
    cp.product_confirmation()
    cp.get_screenshot()

    driver.quit()