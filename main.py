from secrets import URL, LOGIN_URL, USERNAME, PASSWORD, class_name
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import schedule
import time

# Authentication
def authenticate():
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()
    return driver

# Parser
def parse_page(driver, class_name):
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    value = soup.find('div', {'class': class_name}).text.strip()
    print('Result: ', value)
    return value

# Notification sending function
def send_notification():
    print('Новый урок')

# Task planning service
def job():
    driver = authenticate()
    value = parse_page(driver, class_name)

    if int(value) > 0:
        send_notification()
    driver.quit()


schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# Sending a notification
# def send_notification(value):
    # code to send notification