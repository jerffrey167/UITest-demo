from  selenium.webdriver.support.wait import WebDriverWait
from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.implicitly_wait(5)

driver.get('http://www.baidu.com')
#浏览器打开百度
driver.find_element(By.ID,'kw').send_keys('id定位')
#ID定位搜索框输入 selenium
sleep(2)
driver.find_element(By.ID,'kw').send_keys('点点点')
sleep(1)
driver.find_element(By.ID,'kw').send_keys(Keys.ENTER)
sleep(4)
#回车按钮

