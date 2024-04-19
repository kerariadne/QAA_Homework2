from selenium.webdriver.common.by import By


class Locators:
    men_button = (By.ID, 'ui-id-5')
    card = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[2]/div[3]/div/div/ol/li[1]/div/div/strong/a')
    cart = (By.ID, 'product-addtocart-button')
    error_text = (By.ID, 'super_attribute[93]-error')