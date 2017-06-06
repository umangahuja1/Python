'''
This script let you search anything on browser from terminal
'''

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome() 
driver.get('http://www.google.com/xhtml');
print('Browser open...')
sleep(2) 
search_box = driver.find_element_by_name('q')
query=input('enter the thing you want to search:')
search_box.send_keys(query)
sleep(2)
search_box.submit()
print('Searched...')
sleep(5) 
print('Bye Bye.')
sleep(2)
driver.quit()
print('Game Over')
