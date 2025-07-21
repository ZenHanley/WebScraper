#-- =========================================== #
#--                  Imports                    #
#-- =========================================== #
import time
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#-- =========================================== #
#--           Set Service and Driver            #
#-- =========================================== #

# Initialize the Chrome driver with the path to Chromedriver
service = Service(executable_path="chromedriver.exe")
driver =  webdriver.Chrome(service=service)
# Page load with Cloudflare bypass
driver.get(data.start)
# Maximize the browser window to ensure all elements are visible to be scraped
driver.maximize_window()
#Wait for the page to load
time.sleep(0.5)