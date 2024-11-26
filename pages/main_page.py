from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
# from pages.login_page import LoginPage


class MainPage(Base):

    url = 'https://www.portovino.co.il/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    agree_button = '//span[@class="l7_2fn wixui-button__label" and text()="I Agree"]'

    #getters

    def get_agree_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_button)))


    #actions

    def click_agree_button(self):
        self.get_agree_button().click()
        print("Click agree button")


    #methods

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_agree_button()