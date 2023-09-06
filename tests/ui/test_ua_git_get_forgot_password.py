import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


@pytest.mark.ui
def test__forgot_password():
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/tests_practice/" + "chromedriver")
    )
    driver.get("https://github.com/login")
    driver.find_element(By.ID, "forgot-password").click()
    driver.implicitly_wait(4)

    assert driver.title == "Forgot your password? · GitHub"

    driver.close()
