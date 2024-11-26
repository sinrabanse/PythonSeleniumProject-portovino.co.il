import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from pages.cart_page import CartPage
# from pages.client_info_page import ClientInfoPage
# from pages.finish_page import FinishPage
# from pages.login_page import LoginPage
from pages.main_page import MainPage
# from pages.payment_page import PaymentPage

@pytest.mark.run(order=1)
def test_buy_product_1(set_up, set_group):
    driver = webdriver.Chrome()

    # login = LoginPage(driver)
    # login.autorization()

    mp = MainPage(driver)
    mp.start()

    # cp = CartPage(driver)
    # cp.product_confirmation()
    #
    # cip = ClientInfoPage(driver)
    # cip.fill_client()
    #
    # pay = PaymentPage(driver)
    # pay.payment()
    #
    # fp = FinishPage(driver)
    # fp.finish()


    time.sleep(5)
    driver.quit()

# @pytest.mark.run(order=2)
# def test_buy_product_2(set_up):
#     driver = webdriver.Chrome()
#
#     login = LoginPage(driver)
#     login.autorization()
#
#     mp = MainPage(driver)
#     mp.add_to_cart_product_2()
#
#     cp = CartPage(driver)
#     cp.product_confirmation()
#
#     # time.sleep(5)
#     driver.quit()
#
# @pytest.mark.run(order=3)
# def test_buy_product_3():
#     driver = webdriver.Chrome()
#
#     login = LoginPage(driver)
#     login.autorization()
#
#     mp = MainPage(driver)
#     mp.add_to_cart_product_3()
#
#     cp = CartPage(driver)
#     cp.product_confirmation()
#
#     # time.sleep(5)
#     driver.quit()