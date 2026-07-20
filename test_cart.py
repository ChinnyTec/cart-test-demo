from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart():
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10)  # Generous wait time
    
    driver.get("https://www.saucedemo.com/")
    
    # Log in
    driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
    
    # Click the exact backpack add-to-cart button using data-test attributes
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # Verify the badge
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    assert cart_badge == "1"
    driver.quit()