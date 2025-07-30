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
def info_enter(driver, By, time, email_data, email_input, password_data, password_input):
    driver.find_element(By.NAME,email_data).send_keys(email_input)
    driver.find_element(By.NAME,password_data).send_keys(password_input)
    time.sleep(0.5)