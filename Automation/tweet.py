'''
This script is created to tweet from terminal either manually or through clipboard text as per user's choice 
'''
from selenium import webdriver
from time import sleep
import pyperclip

usr=input('Enter user id :')
pwd=input('Enter password :')
choice=input('Enter choice of posting \n1.manual\n2.clipboard\n')

if int(choice)==1:
	msg=input('Enter tweet here:')
else:
	msg=pyperclip.paste()

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

c=driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
c.click()
print("Twitter Logged ")

d=driver.find_element_by_id('tweet-box-home-timeline')
d.send_keys(msg)
print("Text entered")

e=driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
e.click()
print("Posted")

sleep(5)
driver.quit()
print("Game Over")
