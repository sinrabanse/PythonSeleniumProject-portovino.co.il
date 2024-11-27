import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base


class WhiskyPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    sidebar_category_irish = '//label[@class="wixSdkShowFocusOnSibling o8pQoW" and text()="Irish Whisky"]'
    sorting_field = '//span[@class="srnd0jq"]'
    sorting_high_to_low = '//span[@class="saOxbFe oHyUmpe---typography-11-runningText oHyUmpe---priority-7-primary s_Qy4ho" and text()="Price (high to low)"]'
    product_1_card = '(//div[@data-hook="ImageUiTpaWrapperDataHook.Wrapper_0"])[1]'
    product_1_quick_view = '(//button[@data-hook="product-item-quick-view-button"])[1]'
    product_1_iframe = '//iframe[@name="tpaModal_rtby_comp-kcn3043y"]'
    product_1_name = '//h1[@data-hook="product-title"]'
    product_1_price = '//span[@data-hook="formatted-primary-price"]'
    quick_add_to_cart = '//button[@data-hook="add-to-cart"]'
    to_cart_button = '//a[@data-hook="cart-icon-button"]'
    product_1_name_in_cart = '//p[@data-hook="CartItemDataHook.name"]'
    product_1_price_in_cart = '//span[@data-hook="CartItemDataHook.price"]'

    #getters

    def get_sidebar_category_irish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sidebar_category_irish)))

    def get_sorting_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_field)))

    def get_sorting_high_to_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_high_to_low)))

    def get_product_1_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_card)))

    def get_product_1_quick_view(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_quick_view)))

    def get_product_1_iframe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_iframe)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    def get_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name)))

    def get_quick_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quick_add_to_cart)))

    def get_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart_button)))

    def get_product_1_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_in_cart)))

    def get_product_1_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_in_cart)))


    #actions

    def click_sidebar_category_irish(self):
        self.get_sidebar_category_irish().click()
        print("Choose irish category")

    def click_sorting_field(self):
        self.get_sorting_field().click()
        print("Click on sorting field")

    def click_sorting_high_to_low(self):
        self.get_sorting_high_to_low().click()
        print("Choose sorting by price from high to low")

    def move_cursor_to_product_1_card(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_product_1_card()).perform()

    def click_product_1_quick_view(self):
        self.get_product_1_quick_view().click()
        print("Click quick view of product 1")

    def switch_to_iframe_product_1(self):
        self.driver.switch_to.frame(self.get_product_1_iframe())
        print("Switched to product 1 iframe")

    def write_product_1_price(self):
        self.product_1_price = self.get_product_1_price().text
        print(f"Price of product 1 = {self.product_1_price}")

    def write_product_1_name(self):
        self.product_1_name = self.get_product_1_name().text
        print(f"Name of product 1 = {self.product_1_name}")

    def click_quick_add_to_cart(self):
        self.get_quick_add_to_cart().click()
        print("Click add to cart")

    def click_to_cart_button(self):
        self.get_to_cart_button().click()
        print("Click to cart button")

    def check_product_1_name_in_cart(self):
        self.assert_word(word = self.get_product_1_name_in_cart(), result = self.product_1_name)

    def check_product_1_price_in_cart(self):
        self.assert_word(word = self.get_product_1_price_in_cart(), result = self.product_1_price)


    #methods

    def buy_product_1(self):
        self.get_current_url()
        self.click_sidebar_category_irish()
        self.click_sorting_field()
        self.click_sorting_high_to_low()
        self.move_cursor_to_product_1_card()
        self.click_product_1_quick_view()
        self.switch_to_iframe_product_1()
        self.write_product_1_price()
        self.write_product_1_name()
        self.click_quick_add_to_cart()
        self.driver.refresh() # пытался решить через iframe обратно вернуться и не смог к сожалению, по этому просто обновляю страницу
        self.click_to_cart_button()
        self.assert_url("https://www.portovino.co.il/cart")
        self.check_product_1_name_in_cart()
        self.check_product_1_price_in_cart()