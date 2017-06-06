'''
This script is created to login-logout of facebook from terminal
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')
print ("Opened facebook...")
sleep(1)

a = driver.find_element_by_id('email')
a.send_keys(usr)
print ("Email Id entered...")
sleep(1)

b = driver.find_element_by_id('pass')
b.send_keys(pwd)
print ("Password entered...")

c = driver.find_element_by_id('loginbutton')
c.click()

print ("Logged In...")

sleep(20)

d= driver.find_element_by_id("userNavigationLabel")
d.click()
sleep(10)

e=driver.find_element_by_xpath("//a[contains(@data-gt,'menu_logout')]")
e.click()
sleep(5)
print("Logged Out")

driver.quit()
print("Game Over...")
