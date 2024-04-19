from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


def example():
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()


def click_on_men():
    driver.find_element(*Locators.men_button).click()


def click_on_card():
    driver.find_element(*Locators.card).click()


def click_on_cart():
    driver.find_element(*Locators.cart).click()


def get_error_text():
   element = WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.error_text))
   return element.text

def webdriver_quit():
    driver.quit()
