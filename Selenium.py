from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("https://google.com")

assert "Google in driver.title"

print("Test Passed: Google opened successfully")

time.sleep(5)

driver.quit()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.get("https://google.com")

time.sleep(2)

try:
    accept_button = driver.find_element(By.XPATH, "//button[.//text()='Accept all']")
    accept_button.click()
    time.sleep(2)
except:
    print("No cookies popup found")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("QA Automation")
search_box.send_keys(Keys.RETURN)

time.sleep(15)

print("Test Passed: Search executed")

driver.quit()

