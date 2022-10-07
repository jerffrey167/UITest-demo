from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
考试系统的登录+输入框的条件查询+下拉框的条件查询+账号退出
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://192.168.3.12:8100/#/login')
#浏览器打开考试系统
sleep(2)
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
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 40px')]/span[text()='考试管理']").click()
sleep(1)
######################考试类型搜索框
driver.find_element(By.XPATH,'//input[@placeholder="开放类型"]').click()
sleep(1)
ExamSearch=driver.find_element(By.XPATH,"//div[@class='el-select-dropdown el-popper'and@x-placement]/div")
ExamSearch1=driver.find_element(By.XPATH,"//span[text()='完全开放']//..").click()
sleep(1)
######################考试名称搜索框
driver.find_element(By.XPATH,'//input[@placeholder="搜索考试名称"]').send_keys('演示考试')
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