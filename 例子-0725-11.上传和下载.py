#coding=utf-8

from selenium import  webdriver
import time
br=webdriver.Chrome()
#上传
# br.get("http://127.0.0.1/12.html")
# time.sleep(2)
# #定位上传按钮
# br.find_element_by_name('file').send_keys("F:\\abc.png")
# time.sleep(2)
# br.quit()
#下载
br.get("https://pypi.org/project/selenium/#files")
br.find_element_by_link_text('selenium-3.141.0.tar.gz').click()
time.sleep(10)
print('ok')