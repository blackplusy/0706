#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# br=webdriver.Chrome()
# br.get("https://www.baidu.com")
# br.maximize_window()
# element=br.find_element_by_link_text("新闻")
#单击元素
# ActionChains(br).click(element).perform()
#元素上按下左键不放
# element=br.find_element_by_id('s-usersetting-top')
# ActionChains(br).click_and_hold(element).perform()
#单击右键
# ActionChains(br).context_click(element).perform()
#双击元素
# ActionChains(br).double_click(element).perform()

br=webdriver.Chrome()
br.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
br.maximize_window()
br.switch_to.frame('iframeResult')
source=br.find_element_by_id('draggable')
target=br.find_element_by_id('droppable')
action=ActionChains(br)
action.drag_and_drop(source,target).perform()