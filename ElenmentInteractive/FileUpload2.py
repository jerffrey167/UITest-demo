from  selenium import  webdriver
from  selenium.webdriver.common.by import By
from  time import  sleep
from pywinauto.keyboard import send_keys

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
###############################


# 创建操作桌面的对象
driver.find_element(By.XPATH,"//span[text()='导入']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='上传导入']/..").click()
sleep(1)

#获取文件路径填写输入框并点击
send_keys(r"C:\Users\Administrator\Pictures\R-C.png")
#在文件路径填写输入框输入文件存在的路径
send_keys("{VK_RETURN}")
sleep(2)
driver.find_element(By.XPATH,"//div[@aria-label='导入试题']/div/button").click()
################################账号注销
driver.find_element(By.XPATH,"//div[text()=' 超管A ']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='退出登录']//..").click()
##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器