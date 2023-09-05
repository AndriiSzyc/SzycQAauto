import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_get_create_account_page():
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/tests_practice/" + "chromedriver")
    )
    driver.get("https://github.com/login")
    elem = driver.find_element(By.XPATH, "//*[@id='login']/p/a")
    elem.click()
    driver.implicitly_wait(4)

    assert driver.title == "Join GitHub · GitHub"

    driver.close()
