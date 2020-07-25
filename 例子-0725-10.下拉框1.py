#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
br=webdriver.Chrome()
br.get("http://127.0.0.1/11.html")
#1.通过send_keys
# br.find_element_by_id('select').send_keys('bbb')

#2.二次定位操作
# br.find_element_by_id('select').find_element_by_xpath('//option[@value="10"]').click()

#3.select 类
#实例化select类对象
selector=Select(br.find_element_by_id('select'))
#a.通过索引进行选择
# selector.select_by_index("0")
#b.通过属性的值进行选择
# selector.select_by_value('20')
#c.通过显示的text进行选择
selector.select_by_visible_text('aaa')


