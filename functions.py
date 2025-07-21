#-- =========================================== #
#--              Clicking Buttons               #
#-- =========================================== #
def click(driver, By, time, data):
    #Clicking login button
    driver.find_element(By.CSS_SELECTOR,data).click()
    time.sleep(0.5)
    
#-- =========================================== #
#--            Entering Information             #
#-- =========================================== #
def info_enter(driver, By, time, info, data):
    driver.find_element(By.NAME,info).send_keys(data)
    time.sleep(0.5)