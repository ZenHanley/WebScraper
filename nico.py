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

# Maximize the browser window to ensure all elements are visible
driver.maximize_window()

# Wait for the page to load completely
time.sleep(3)

# Find and print the titles of the lessons
titles = driver.find_elements(By.CLASS_NAME, "t1duk5k2")
for title in titles:
    print(title.text)

main = driver.find_elements(By.XPATH, '//*[@id="courses"]/section[2]/section[1]/div/ul/div/li[1]/a/div[2]/div[2]')
for m in main:
    scores = m.find_elements(By.TAG_NAME, "span")
    for s in scores:
        print(s.text)