#-- =========================================== #
#--                   Imports                   #
#-- =========================================== #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
from ..WebScraper import data

#Used to wrap content
wrap = True

#-- =========================================== #
#--           Set Service and Driver            #
#-- =========================================== #

# Initialize the Chrome driver with the path to Chromedriver
service = Service(executable_path="chromedriver.exe")
driver =  webdriver.Chrome(service=service)
# Page load with Cloudflare bypass
driver.get(start)
# Maximize the browser window to ensure all elements are visible to be scraped
driver.maximize_window()
#Wait for the page to load
time.sleep(0.5)

#-- =========================================== #
#--             Entering Information            #
#-- =========================================== #
if wrap == True:
    #Find and enter the email
    driver.find_element(By.NAME,"username").send_keys(email)
    time.sleep(0.5)

    #Find and enter the password
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep(0.5)

#-- =========================================== #
#--               Clicking Buttons              #
#-- =========================================== #
if wrap == True:
    #Clicking login button
    driver.find_element(By.CSS_SELECTOR,".sr1l9xy.primary.b17wp39w").click()
    time.sleep(0.5)
    
    #Clicking Confirm Button
    driver.find_element(By.CSS_SELECTOR,".s13pardp.l133n852.sr1l9xy.primary.b17wp39w").click()
    time.sleep(0.5)

#-- =========================================== #
#--                A2 Page Redirect             #
#-- =========================================== #
if wrap == True:
    driver.get(A2_url)
    time.sleep(1)

#-- =========================================== #
#--           Find and Print Data               #
#-- =========================================== #
if wrap == True:
    # Find and print the scores
    scores = driver.find_elements(By.CSS_SELECTOR, ".s1l6w876.d1sa64gj")
    titles = driver.find_elements(By.CLASS_NAME, "t1duk5k2")
    
    for score, title in zip(scores, titles):
        print(title.text, score.text)