from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find field in which we will enter incorrect user-name or e-mail address
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter incorrect user-name or e-mail address
        login_elem.send_keys(username)

        # Find field in which we will enter incorrect Password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter incorrect Password
        pass_elem.send_keys(password)

        # Find "Sign in" button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate click left-mouse button
        btn_elem.click()

    # Check that name of page is what we expect
    def check_title(self, expected_title):
        return self.driver.title == expected_title
