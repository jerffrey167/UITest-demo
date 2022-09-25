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
driver.find_element(By.LINK_TEXT,'新闻').click()
#链接文本定位，所填写内容必须为全部内容
sleep(2)
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器