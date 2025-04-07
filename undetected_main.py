import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

try:
    driver.get("https://www.google.com")

    time.sleep(2)  # Wait for the page to load

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Black Desert Online")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)  # Wait for the results to load
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    first_result.click()

    time.sleep(5)  # Wait to see if it opens 

finally:
    driver.quit()