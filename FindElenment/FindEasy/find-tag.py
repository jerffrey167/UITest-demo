from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://www.baidu.com')
#浏览器打开百度
sleep(2)
inputs = driver.find_elements(By.TAG_NAME,'input')
#tag定位搜索框输入 tag定位
# 如果定位到的元素不止1个，那么就需要用到find_elements 的方法
sleep(2)
for input in inputs:
    print(input.get_dom_attribute('id'))
    if (input.get_dom_attribute('id')=='kw'):
        input.send_keys('演示id和tag综合获取元素')
#通过for 循环 二次通过id定位的方式获取到需要的元素
sleep(2)
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器
