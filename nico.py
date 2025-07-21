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
    url="https://learngerman.dw.com/en/nicos-weg/c-36519797"
    email= "zenhanleyreisser@gmail.com"
    password= "Gragknock82"

#-- =========================================== #
#--           Set Service and Driver            #
#-- =========================================== #
if wrap == True:
    # Initialize the Chrome driver with the path to Chromedriver
    service = Service(executable_path="chromedriver.exe")
    driver =  webdriver.Chrome(service=service)
    # Page load with Cloudflare bypass
    driver.get(url)
    # Maximize the browser window to ensure all elements are visible to be scraped
    driver.maximize_window()
    #Wait for the page to load
    time.sleep(2)

#-- =========================================== #
#--                 Navigate Login              #
#-- =========================================== #
if wrap == True:
    # Find and click the menu button
    nav = driver.find_element(By.CLASS_NAME, "s18n1k0y")
    nav.click()
    time.sleep(0.5)

    # Find and click the login button
    buttons = driver.find_elements(By.CLASS_NAME, "n1ydif5t")
    #loops through the button menu and clicks the login button
    for button in buttons:
        if button.text == "Login":
            button.click()
            time.sleep(2)
            break

#-- =========================================== #
#--             Entering Information            #
#-- =========================================== #
if wrap == True:
    #Find and enter the email
    email_field = driver.find_element(By.NAME,"username")
    email_field.send_keys(email)
    time.sleep(0.5)

    #Find and enter the password
    password_field = driver.find_element(By.NAME,"password")
    password_field.send_keys(password)
    time.sleep(0.5)

#-- =========================================== #
#--               Clicking Buttons              #
#-- =========================================== #
if wrap == True:
    #Clicking login button
    form = driver.find_element(By.TAG_NAME,"form")
    login_buttons = form.find_element(By.TAG_NAME,"button")
    login_buttons.click()
    time.sleep(5)
    
    #Clicking Confirm Button
    confirm = driver.find_elements(By.TAG_NAME, "a")
    for c in confirm:
        if c.text == "Ok":
            c.click()
            break
    time.sleep(5)

#-- =========================================== #
#--           Find and Print Data               #
#-- =========================================== #
if wrap == True:
    # Find and print the titles of the lessons
    titles = driver.find_elements(By.CLASS_NAME, "t1duk5k2")
    for title in titles:
        print(title.text)

    # Find and print the scores
    scores = driver.find_elements(By.CLASS_NAME, "s1l6w876 d1sa64gj")                
    for score in scores:
        scores = s.find_elements(By.TAG_NAME, "span")
        for s in scores:
            print(s.text)