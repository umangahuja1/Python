'''
This script is created to tweet image from terminal
'''

from selenium import webdriver
from time import sleep

usr=input("Enter email id:")
pwd=input("Enter Password:")
path=input('Enter the path of file you want to post:')+"/"+input('Enter file name:')

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
print("Twitter Logged In")

d=driver.find_element_by_css_selector('input.file-input.js-tooltip')
d.send_keys(path)
print("File entered")

e=driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
e.click()
print("Posted")

sleep(10)
driver.quit()
print("Game Over")

