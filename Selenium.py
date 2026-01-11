from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("https://google.com")

assert "Google in driver.title"

print("Test Passed: Google opened successfully")

time.sleep(5)

driver.quit()
