from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class StartPage(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self) -> None:
        super().__init__()
        self.driver.get(StartPage.URL)

    def try_login(self, username):
        self.driver.find_element(
            by=By.ID, value="nav-link-accountList-nav-line-1"
        ).click()

        self.driver.find_element(by=By.ID, value="ap_email").send_keys(username)
        self.driver.find_element(by=By.ID, value="continue").click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def go_cart(self):
        self.driver.find_element(by=By.ID, value="nav-cart-count").click()

    def check_text_empty_cart(self, expected_title):
        message = self.driver.find_element(by=By.TAG_NAME, value="h2")
        value = message.text
        return value == expected_title

    def search_amzn(self, text):
        self.driver.find_element(by=By.ID, value="twotabsearchtextbox").send_keys(text)
        self.driver.find_element(by=By.ID, value="nav-search-submit-button").click()

    @staticmethod
    def implicitly_wait(time_wait):
        time.sleep(time_wait)
