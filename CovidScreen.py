from selenium import webdriver
from dotenv import load_dotenv
import time
import os

load_dotenv()
STUDENT_ID = os.getenv('STUDENT_ID')
DOB = os.getenv('DOB')

url = 'https://gecdsb-covid-assessment.azurewebsites.net/?NoLogin=1'
driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_id('NoLoginID').send_keys(STUDENT_ID)
driver.find_element_by_id('NoLoginDOB').send_keys(DOB)
driver.find_element_by_id('ContinueButton').click()

for i in range(1, 7):
    time.sleep(1)
    driver.find_element_by_css_selector(
        "label[for='AdditionalQuestion" + str(i) + "No']"
    ).click()

time.sleep(1)
driver.find_element_by_id('CheckNone').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div[2]/div[7]/button').click()
