from  selenium import  webdriver
from  selenium.webdriver.common.by import By
from  time import  sleep

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://120.46.215.163:8102/#/login')
#浏览器打开考试系统
driver.implicitly_wait(6)
#隐式等待
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('admin')
#用户名
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('admin')
#密码
driver.find_element(By.XPATH,'//button[@type="button"]').click()
#登录按钮
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 20px')]/span[text()='考试管理']").click()
#点击考试管理模块
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 40px')]/span[text()='试题管理']").click()
sleep(1)
################################账号注销
driver.find_element(By.XPATH,"//div[text()=' 超管A ']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='退出登录']//..").click()
##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器