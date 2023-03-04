from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://120.46.215.163:8102/#/login')
#浏览器打开考试系统
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('s2')
#用户名
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('123456')
#密码
driver.find_element(By.XPATH,'//button[@type="button"]').click()
sleep(2)

e1=driver.find_element(By.CSS_SELECTOR,'div#size-select')
ActionChains(driver).move_to_element(e1).perform()
###########鼠标悬停


sleep(2)

