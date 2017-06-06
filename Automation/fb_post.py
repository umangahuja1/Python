'''
This script is created to post status on fb from terminal
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
message=input('Enter the message to be posted:')

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

post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.send_keys(message)
sleep(3)
print ("Text entered to be posted")

post_it=driver.find_element_by_xpath("//button[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
post_it.click()
print ('Posted')

sleep(5)
driver.quit()
print("Game Over...")

