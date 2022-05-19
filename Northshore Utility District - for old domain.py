# NUD's domain updated. The page is no longer accessible.
# Generic user name and password to protect privacy.
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time

driver = webdriver.Chrome() 
driver.get('https://customers.nud.net/login.aspx') 
time.sleep(2)

user_name = driver.find_element_by_name('ctl00$MainContentPlaceHolder$Login1$UserName')
user_name.send_keys('ABC')
password = driver.find_element_by_name('ctl00$MainContentPlaceHolder$Login1$Password')
password.send_keys('ABC')
time.sleep(1)
button = driver.find_element_by_name('ctl00$MainContentPlaceHolder$Login1$LoginButton')
time.sleep(1)
button.click()
time.sleep(1)
style = driver.find_element_by_tag_name('p') # 解析网页并提取第一个<lable>标签
print(style.text) # 打印label的文本
driver.close() # 关闭浏览器