from datetime import datetime
import datetime
import allure


class Base():

    def __init__(self, driver ):
        self.driver = driver

    # Method to get current URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    # Method to assert words

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good value word {value_word} = {result}")


    #Method to make screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('../screen/' + name_screenshot)

    #Method assert URL

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    def assert_url_start(self, result):
        get_url = self.driver.current_url
        assert get_url.startswith(result), f"Expected URL to start with {result}, but got {get_url}"
        print("Good value URL")
