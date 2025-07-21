from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  
import time


# Initialize the Chrome driver with the path to Chromedriver
service = Service(executable_path="chromedriver.exe")
driver =  webdriver.Chrome(service=service)

# Url to Nico's Weg A2
url="https://learngerman.dw.com/en/nicos-weg/c-36519797"

# Page load with Cloudflare bypass
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Find the input element by its class name
input_element = driver.find_element(By.CLASS_NAME, "ckvibhv")
print(input_element)