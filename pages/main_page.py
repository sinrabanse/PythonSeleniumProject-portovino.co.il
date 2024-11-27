from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = 'https://www.portovino.co.il/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    agree_button = '//span[@class="l7_2fn wixui-button__label" and text()="I Agree"]'
    whisky_page_header = '//p[@id="i98d56oi1label"]'
    whisky_page_title = ('(//span[@class="wixui-rich-text__text" and text()="Whisky"])[1]')

    #getters

    def get_agree_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_button)))

    def get_whisky_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.whisky_page_header)))

    def get_whisky_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.whisky_page_title)))


    #actions

    def click_agree_button(self):
        self.get_agree_button().click()
        print("Click agree button")

    def click_whisky_page_header(self):
        self.get_whisky_page_header().click()
        print("Click whisky page in the header")


    #methods

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_agree_button()

    def go_to_whisky_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_agree_button()
        self.click_whisky_page_header()
        self.assert_word(self.get_whisky_page_title(), "Whisky")
        self.assert_url("https://www.portovino.co.il/whisky")