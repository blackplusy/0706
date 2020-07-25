#coding=utf-8
from selenium import webdriver

import  time
br=webdriver.Chrome()

br.get("http://127.0.0.1/1.html")

time.sleep(2)

br.find_element_by_id('test1').click()
#获取打开浏览器的窗口
windowtabs=br.window_handles
print(windowtabs)
#获取当前浏览器的窗口
currenttab=br.current_window_handle
print(currenttab)
#切换标签
br.switch_to.window(windowtabs[0])
time.sleep(2)
br.switch_to.window(windowtabs[1])
