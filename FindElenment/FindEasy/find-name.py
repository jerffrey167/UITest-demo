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
driver.find_element(By.NAME,'wd').send_keys('name定位')
#name定位搜索框输入 selenium
sleep(2)
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器