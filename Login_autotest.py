from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



time.sleep(15)

message = driver.find_element(By.ID, "flash").text

assert "You logged into a secure area!" in message

print("Test Passed: Login successful")

time.sleep(3)
driver.quit()
