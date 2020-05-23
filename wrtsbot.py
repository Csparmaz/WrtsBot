from selenium import webdriver
import random
import time
emailGmailFormat = "@gmail.com"
joinURL = input('What is the group link?')
while True:
    driver = webdriver.Chrome()
    driver.get('https://leren.wrts.nl/registreren')

    #Making a fake first name
    firstName = random.randint(1, 10000)

    #Making a fake last name
    lastName = random.randint(1, 10000)
    
    #Entering first name
    element = driver.find_element_by_id("user_first_name")
    element.send_keys(firstName)

    #The same for last name
    element = driver.find_element_by_id("user_last_name")
    element.send_keys(lastName)

    #Making a fake e-mail
    emailName = random.randint(1, 10000)


    #Entering e-mail
    element = driver.find_element_by_id("user_email")
    element.send_keys(emailName)
    element.send_keys(emailGmailFormat)
    
    #Entering password (No need to generate)
    #Password is always: 69420666      
    passwordName = 69420666

    element = driver.find_element_by_id("user_password")
    element.send_keys(passwordName)    

    #Setting the date (day)
    select = Select(driver.find_element_by_id('user_birthday_3i'))

    select.select_by_visible_text('11')

    #Setting the date (month)
    select = Select(driver.find_element_by_id('user_birthday_2i'))

    select.select_by_visible_text('september')

    #Setting the date (year)
    select = Select(driver.find_element_by_id('user_birthday_1i'))

    select.select_by_visible_text('2001')

    #Making the account

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










