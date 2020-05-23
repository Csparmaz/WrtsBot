from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import time

i = 7
UrlToSearch = "https://leren.wrts.nl/registreren"
print(UrlToSearch)
joinURL = input('What is the group link?')
while i == 7:
    driver = webdriver.Chrome()
    driver.get(UrlToSearch)
    driver.set_page_load_timeout(1)

    #Making a fake first name
    firstName = random.randint(1, 10000)

    #Making a fake last name
    lastName = random.randint(1, 10000)

    #Opening and entering the first name
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'user_first_name')))
    element = driver.find_element_by_id("user_first_name")
    element.send_keys(firstName)

    #The same for last name
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'user_last_name')))
    element = driver.find_element_by_id("user_last_name")
    element.send_keys(lastName)

    #Making a fake e-mail
    emailName = random.randint(1, 10000)
    emailGmailFormat = "@gmail.com"

    #Entering e-mail
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'user_email')))
    element = driver.find_element_by_id("user_email")
    element.send_keys(emailName)
    element.send_keys(emailGmailFormat)
    emailGmailFormat = "@gmail.com"

    #Entering password (No need to generate)
    #Password is always: 69420666      
    passwordName = 69420666
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'user_password')))
    element = driver.find_element_by_id("user_password")
    element.send_keys(passwordName)    

    #Setting the date (day)
    wait = WebDriverWait(driver, 10)
    select = Select(driver.find_element_by_id('user_birthday_3i'))

    select.select_by_visible_text('11')

    #Setting the date (month)
    wait = WebDriverWait(driver, 10)
    select = Select(driver.find_element_by_id('user_birthday_2i'))

    select.select_by_visible_text('september')

    #Setting the date (year)
    wait = WebDriverWait(driver, 10)
    select = Select(driver.find_element_by_id('user_birthday_1i'))

    select.select_by_visible_text('2001')

    #Making the account
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'accept_conditions')))
    element = driver.find_element_by_id("accept_conditions")
    element.send_keys(Keys.ENTER)

    #LAST STEP FOR COMPLETION
    #Setting it to the dashboard
    time.sleep(1)
    driver.get("https://leren.wrts.nl/free_user")
    #Going to dashboard
    driver.get("https://leren.wrts.nl/#profile/dashboard")
    #Entering the group
    driver.get(joinURL)
    
    driver.close()
    print('BOT COMPLETED')
print('epic')










