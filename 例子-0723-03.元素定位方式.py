#coding=utf-8
#导入webdriver
from selenium import webdriver
#定义驱动
br=webdriver.Chrome()
#打开网页
br.get("https://www.baidu.com")
#id定位元素
#定位id值是kw的元素，在里面输入扣你齐瓦
# br.find_element_by_id('kw').send_keys("扣你齐瓦")
# br.find_element_by_id('su').click()
#name定位元素
#定位name值是wd的元素，在里面输入攀娘
# br.find_element_by_name('wd').send_keys("攀娘")
#class定位
#定位class值是s_ipt的元素，里面输入带古拉k
# br.find_element_by_class_name('s_ipt').send_keys("带古拉k")
#tag定位
#通过input标签进行定位
# br.find_element_by_tag_name('input').send_keys("小火龙")
#通过link定位
#通过a标签中的内容进行定位 <a></a>
# br.find_element_by_link_text("新闻").click()
#通过partial_link
#通过a标签中的部分内容进行定位 <a></a>
# br.find_element_by_partial_link_text("闻").click()
#通过xpath
#//* 所有元素中搜索
#[#id='kw'] id的值是kw的
# br.find_element_by_xpath('//*[@id="kw"]').send_keys("塞朗黑")
#通过css进行定位
# #代表id
# .代表class
br.find_element_by_css_selector("#kw").send_keys("aaa")