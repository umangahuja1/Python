'''
THis script let you login to twitter via terminal
'''

from selenium import webdriver
from time import sleep

usr=input("Enter email id:")
pwd=input("Enter Password:")

driver=webdriver.Chrome()
driver.get('https://twitter.com/login')
print("Twitter Opened")

sleep(2)

a = driver.find_element_by_class_name("js-username-field")
a.send_keys(usr)
print("Id Entered")
sleep(1)

b = driver.find_element_by_class_name("js-password-field")
b.send_keys(pwd)
print("Password Entered")

c=driver.find_element_by_css_selector("button.submit.btn.primary-btn")
c.click()
print("Twitter Logged ")

sleep(5)
driver.quit()
print("Game Over")

