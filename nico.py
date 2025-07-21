#-- =========================================== #
#--                   Imports                   #
#-- =========================================== #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time

#Used to wrap content
wrap = True

#-- =========================================== #
#--                    Data                     #
#-- =========================================== #
if wrap == True:
    # Url to Nico's Weg A2
    start="https://learngerman.dw.com/en/user/login"
    email= "zenhanleyreisser@gmail.com"
    password= "Gragknock82"
    A2_url="https://learngerman.dw.com/en/nicos-weg/c-36519797"

#-- =========================================== #
#--           Set Service and Driver            #
#-- =========================================== #
if wrap == True:
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
    form = driver.find_element(By.TAG_NAME,"form")
    login_buttons = form.find_element(By.TAG_NAME,"button")
    login_buttons.click()
    time.sleep(0.5)
    
    #Clicking Confirm Button
    confirm = driver.find_elements(By.TAG_NAME, "a")
    for c in confirm:
        if c.text == "Ok":
            c.click()
            break
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