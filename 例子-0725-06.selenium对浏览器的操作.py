#coding=utf-8
from selenium import  webdriver
import time
br=webdriver.Chrome()
# br.get("https://www.baidu.com")
# time.sleep(2)
# br.set_window_size(480,800)
# br.minimize_window()
# time.sleep(2)
# br.maximize_window()
url1='https://www.baidu.com'
br.get(url1)
url2='https://www.4399.com'
br.get(url2)
time.sleep(1)
br.back()
time.sleep(1)
br.forward()
time.sleep(1)
br.refresh()
br.get_screenshot_as_file('F:\\abc.png')
print('yes')


