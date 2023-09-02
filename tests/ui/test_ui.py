import pytest

# modules for communication with browser-driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# module for searching elements by certain attributs
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_check_incorrect_username():
    # creating an object to controle browser
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/SzycQAauto/" + "chromedriver")
    )

    # open https://github.com/login page
    driver.get("https://github.com/login")

    # find the field in which we will enter the wrong username or postal address
    login_elem = driver.find_element(By.ID, "login_field")

    # enter the wrong username or email address
    login_elem.send_keys("myemail@mistakeinemail.com")

    # find the field in which we will enter the wrong password
    pass_elem = driver.find_element(By.ID, "password")
    # enter the wrong password
    pass_elem.send_keys("myemail@mistakeinemail.com")

    # find button 'Sign in'
    btn_elem = driver.find_element(By.NAME, "commit")
    # click on the left mouse button
    btn_elem.click()

    # Check that name of page is what we expect
    assert driver.title == "Sign in to GitHub · GitHub"

    # browser close
    driver.close()
