from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_add_to_cart():
    # 1. Set up headless options for the GitHub cloud environment
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 2. Initialize the driver with the headless options
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10) # Generous wait time

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
# Assignment Pipeline Verification Entry