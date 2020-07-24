#coding=utf-8

from selenium import  webdriver

br=webdriver.Chrome()

br.get("https://www.baidu.com")

# br.find_element_by_css_selector('input').send_keys("aaa")
# br.find_element_by_css_selector("#kw").send_keys("aaa")
# br.find_element_by_css_selector(".s_ipt").send_keys("simida")
# br.find_element_by_css_selector("[name='wd']").send_keys("haleshao")
# br.find_element_by_css_selector("input.s_ipt").send_keys("memeda")
# br.find_element_by_css_selector("input#kw").send_keys('ohayo')
# br.find_element_by_css_selector("input[name='wd']").send_keys("ooo")
br.find_element_by_css_selector("input[autocomplete]").send_keys("123")