from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
考试系统的登录+输入框的条件查询+账号退出
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://www.baiud.com')
#浏览器打开百度
sleep(2)
driver.find_element(By.XPATH,'//a[@id="s-top-loginbtn"]').click()
#点击登录按钮
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('admin')

##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器