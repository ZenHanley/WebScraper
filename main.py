#-- =========================================== #
#--                   Imports                   #
#-- =========================================== #
from selenium.webdriver.common.by import By 
import time
import data
import driver_setup
import functions

driver = driver_setup.driver

#-- =========================================== #
#--             Entering Information            #
#-- =========================================== #

#Find and enter the email
functions.info_enter(driver, By, time, "username", data.email)

#Find and enter the password
functions.info_enter(driver, By, time, "password", data.password)

#-- =========================================== #
#--               Clicking Buttons              #
#-- =========================================== #

#Clicking login button
functions.click(driver, By, time, ".sr1l9xy.primary.b17wp39w")

#Clicking Confirm Button
functions.click(driver, By, time, ".s13pardp.l133n852.sr1l9xy.primary.b17wp39w")

#-- =========================================== #
#--                A2 Page Redirect             #
#-- =========================================== #
driver.get(data.A2_url)
time.sleep(1)

#-- =========================================== #
#--           Find and Print Data               #
#-- =========================================== #

# Find and print the scores
scores = driver.find_elements(By.CSS_SELECTOR, ".s1l6w876.d1sa64gj")
titles = driver.find_elements(By.CLASS_NAME, "t1duk5k2")

#combines both variables and prints the data
for score, title in zip(scores, titles):
    print(title.text, score.text)