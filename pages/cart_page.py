import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    #locators

    add_giftbox_checkbox = '(//label[@data-testid="checkbox"])[1]'
    checkout_button = '//button[@data-hook="CheckoutButtonDataHook.button"]'
    product_1_name_in_cart = '(//p[@data-hook="CartItemDataHook.name"])[1]'
    product_1_price_in_cart = '(//span[@data-hook="CartItemDataHook.price"])[1]'
    giftbox_name_in_cart = '(//p[@data-hook="CartItemDataHook.name"])[2]'
    giftbox_price_in_cart = '(//span[@data-hook="CartItemDataHook.price"])[2]'
    product_1_name_in_checkout = '(//span[@data-hook="LineItemDataHooks.Name"])[1]'
    product_1_price_in_checkout = '(//span[@data-hook="LineItemDataHooks.Price"])[1]'
    giftbox_name_in_checkout = '(//span[@data-hook="LineItemDataHooks.Name"])[2]'
    giftbox_price_in_checkout = '(//span[@data-hook="LineItemDataHooks.Price"])[2]'

    #getters

    def get_add_giftbox_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_giftbox_checkbox)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self. checkout_button)))

    def get_product_1_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_in_cart)))

    def get_product_1_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_in_cart)))

    def get_giftbox_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.giftbox_name_in_cart)))

    def get_giftbox_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.giftbox_price_in_cart)))

    def get_product_1_name_in_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_in_checkout)))

    def get_product_1_price_in_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_in_checkout)))

    def get_giftbox_name_in_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.giftbox_name_in_checkout)))

    def get_giftbox_price_in_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.giftbox_price_in_checkout)))


    #actions

    def click_add_giftbox_checkbox(self):
        time.sleep(5) # Website is slow, so time is needed in this step
        self.get_add_giftbox_checkbox().click()
        time.sleep(5)  # Website is slow, so time is needed in this step
        print("Click checkbox to add giftbox")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    def write_product_1_price_in_cart(self):
        self.product_1_price_in_cart = self.get_product_1_price_in_cart().text
        print(f"Price of product 1 in cart = {self.product_1_price_in_cart}")

    def write_product_1_name_in_cart(self):
        self.product_1_name_in_cart = self.get_product_1_name_in_cart().text
        print(f"Name of product 1 in cart = {self.product_1_name_in_cart}")

    def write_giftbox_price_in_cart(self):
        self.giftbox_price_in_cart = self.get_giftbox_price_in_cart().text
        print(f"Price of giftbox in cart = {self.giftbox_price_in_cart}")

    def write_giftbox_name_in_cart(self):
        self.giftbox_name_in_cart = self.get_giftbox_name_in_cart().text
        print(f"Name of giftbox in cart = {self.giftbox_name_in_cart}")

    def check_product_1_name_in_checkout(self):
        Base.assert_word(self, word = self.get_product_1_name_in_checkout(), result = self.product_1_name_in_cart)

    def check_product_1_price_in_checkout(self):
        Base.assert_word(self, word = self.get_product_1_price_in_checkout(), result = self.product_1_price_in_cart)

    def check_giftbox_name_in_checkout(self):
        Base.assert_word(self, word = self.get_giftbox_name_in_checkout(), result = self.giftbox_name_in_cart)

    def check_giftbox_price_in_checkout(self):
        Base.assert_word(self, word = self.get_giftbox_price_in_checkout(), result = self.giftbox_price_in_cart)



    #methods

    def product_confirmation(self):
        # Adding giftbox and checking products in cart
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.click_add_giftbox_checkbox()
            self.write_product_1_price_in_cart()
            self.write_product_1_name_in_cart()
            self.write_giftbox_price_in_cart()
            self.write_giftbox_name_in_cart()
            self.click_checkout_button()
            time.sleep(5) # Website is slow, so time is needed
            self.assert_url_start("https://www.portovino.co.il/checkout") # Dynamic URL
            self.check_product_1_name_in_checkout()
            self.check_product_1_price_in_checkout()
            self.check_giftbox_name_in_checkout()
            self.check_giftbox_price_in_checkout()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
