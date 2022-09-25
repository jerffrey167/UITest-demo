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
driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('class定位')
#class定位搜索框输入 class定位
sleep(2)
driver.find_element(By.CLASS_NAME,'s_btn').click()
#class定位搜索按钮  注意当class的那么有空格数时，只要输入其中任何一节就行，但是输入全部是不行的
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器