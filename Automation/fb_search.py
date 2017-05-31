'''
This script is created to search on facebook using terminal
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
 
usr=input('Enter your email id: ')
pwd=input('enter your password: ')
query=input('enter search query: ')


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print("Opened facebook...")

sleep(1)
a = driver.find_element_by_id('email')
a.send_keys(usr)
print("Email Id entered...")

b = driver.find_element_by_id('pass')
b.send_keys(pwd)
print("Password entered...")

c = driver.find_element_by_id('loginbutton')
c.click()
print("Logged In...")

sleep(1)

search_box=driver.find_element_by_name('q')
search_box.send_keys(query)
search_box.submit()
print("Searched...")

sleep(10)

driver.quit()

print("Game Over")

