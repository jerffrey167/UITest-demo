from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
百度网站登录输入框操作
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://www.baidu.com')
#浏览器打开百度
sleep(2)
driver.find_element(By.XPATH,'//a[@id="s-top-loginbtn"]').click()
sleep(1)
#点击弹出登录弹出框
#element=driver.find_element(By.XPATH,"//div[@class='tang-content']")
element=driver.find_element(By.XPATH,"//div[@id='passport-login-pop-dialog']")
element1=element.find_element(By.XPATH,"//input[@id='TANGRAM__PSP_11__userName']").send_keys('admin')
element1=element.find_element(By.XPATH,"//input[@id='TANGRAM__PSP_11__password']").send_keys('123456')
element1=element.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()
sleep(1)
#登录弹出框输入内容


##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器