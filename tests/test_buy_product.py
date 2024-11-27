import time

import pytest
from selenium import webdriver

from base.base_class import Base
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.whisky_page import WhiskyPage


def test_buy_product_1(set_up, set_group):
    driver = webdriver.Chrome()

    mp = MainPage(driver)
    mp.go_to_whisky_page()


    wp = WhiskyPage(driver)
    wp.buy_product_1()

    cp = CartPage(driver)
    cp.product_confirmation()
    cp.get_screenshot()

    time.sleep(5)
    driver.quit()