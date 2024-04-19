from selenium import webdriver
from locators import Locators
from actions import example, click_on_men, click_on_card, click_on_cart, webdriver_quit, get_error_text


def test_registration():
    example()
    click_on_men()

    click_on_card()
    click_on_cart()
    actual_error_text = get_error_text()
    expected_error_text = 'This is a required field.'

    assert expected_error_text in actual_error_text

    webdriver_quit()
