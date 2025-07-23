from selenium.webdriver.common.by import By 
import time
import data
import driver_setup
import functions

#Simplifies Data Tag
driver = driver_setup.driver

#Finds and enters the Email using #data
functions.info_enter(driver, By, time, "username", data.email)

#Finds and enters the Password using #data
functions.info_enter(driver, By, time, "password", data.password)

#Clicks the Login Button
functions.click(driver, By, time, ".sr1l9xy.primary.b17wp39w")

#Clicks the Confirm Button
functions.click(driver, By, time, ".s13pardp.l133n852.sr1l9xy.primary.b17wp39w")

#Transfers to Nicos Weg A2 German Page
driver.get(data.A1_url)
time.sleep(0.5)

#Finds the Lesson Title's and Scores
scores = driver.find_elements(By.CSS_SELECTOR, ".s1l6w876.d1sa64gj")
titles = driver.find_elements(By.CLASS_NAME, "t1duk5k2")

#Combines and Prints previous Properties into one List
for title, score in zip(titles, scores):
    print(title.text, score.text)