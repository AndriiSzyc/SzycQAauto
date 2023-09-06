import pytest

# modules for communication with browser-driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# module for searching elements by certain attributs
from selenium.webdriver.common.by import By


@pytest.mark.ui_amzn
def test_incorrect_username():
    # creating an object to control the browser
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/tests_practice/" + "chromedriver")
    )

    # open https://...
    driver.get("https://www.amazon.com/")

    title = driver.title
    assert title == "Amazon.com. Spend less. Smile more."

    elem = driver.find_element(by=By.ID, value="nav-link-accountList-nav-line-1")
    elem.click()
    title = driver.title
    assert title == "Amazon Sign-In"

    driver.find_element(by=By.ID, value="ap_email").send_keys(
        "myemail@mistakeinemail.com"
    )
    elem = driver.find_element(by=By.ID, value="continue")
    elem.click()

    message = driver.find_element(by=By.CLASS_NAME, value="a-alert-heading")
    value = message.text
    assert value == "There was a problem"

    title = driver.title
    assert title == "Amazon Sign-In"

    # browser close
    driver.close()


@pytest.mark.ui_amzn
def test_empty_cart():
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/tests_practice/" + "chromedriver")
    )

    # open https://...
    driver.get("https://www.amazon.com/")

    title = driver.title
    assert title == "Amazon.com. Spend less. Smile more."

    elem = driver.find_element(by=By.ID, value="nav-cart-count")
    elem.click()

    message = driver.find_element(by=By.TAG_NAME, value="h2")
    value = message.text
    assert value == "Your Amazon Cart is empty"

    driver.close()


@pytest.mark.ui_amzn
def test_search():
    driver = webdriver.Chrome(
        service=Service(r"/home/andrii/QAauto/tests_practice/" + "chromedriver")
    )

    # open https://...
    driver.get("https://www.amazon.com/")

    title = driver.title
    assert title == "Amazon.com. Spend less. Smile more."

    driver.find_element(by=By.ID, value="twotabsearchtextbox").send_keys("tolkien")
    elem = driver.find_element(by=By.ID, value="nav-search-submit-button")
    elem.click()

    title = driver.title
    assert title == "Amazon.com : tolkien"

    driver.close()
