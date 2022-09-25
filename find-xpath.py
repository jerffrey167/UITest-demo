from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://120.46.215.163:8101/#/login')
#浏览器打开百度
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('person')
#用户名
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('person')
#密码
driver.find_element(By.XPATH,'//button[@type="button"]').click()
#登录按钮
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 20px')]/span[text()='在线考试']").click()
#点击在线考试模块
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 40px')]/span[text()='在线考试']").click()
#点击在线考试页面
sleep(1)
driver.find_element(By.XPATH,"//span[text()='去考试']").click()
#点击去考试按钮
sleep(1)
driver.find_element(By.XPATH,"//*[text()=' 开始考试 ']").click()
#点击开始考试按钮
sleep(3)

driver.find_element(By.XPATH,"//*[text()='A.25%  ']//..").click()
#第一题

driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器