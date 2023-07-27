import pytest

# Modules for communication with browser-driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Module for searching elements by certain attributs
from selenium.webdriver.common.by import By

# import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Creating an object to controle browser
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/SzycQAauto/" + "chromedriver")
    )

    # Open https://github.com/login page
    driver.get("https://github.com/login")

    # Find field in which we will enter incorrect user-name or e-mail address
    login_elem = driver.find_element(By.ID, "login_field")
    # Enter incorrect user-name or e-mail address
    login_elem.send_keys("andriiszyc@mistakeinemail.com")

    # Find field in which we will enter incorrect Password
    pass_elem = driver.find_element(By.ID, "password")
    # Enter incorrect Password
    pass_elem.send_keys("wrong password")

    # Find "Sign in" button
    btn_elem = driver.find_element(By.NAME, "commit")
    # Emulate click left-mouse button
    btn_elem.click()

    # Check that name of page is what we expect
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)

    # Close browser
    driver.close()
