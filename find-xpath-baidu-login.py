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
driver.get('http://www.baidu.com')
#浏览器打开百度
sleep(2)
driver.find_element(By.XPATH,'//a[@id="s-top-loginbtn"]').click()
sleep(1)
#点击弹出登录弹出框
element=driver.find_element(By.XPATH,"//div[@class='tang-content']")
element1=element.find_element(By.XPATH,"//input[@id='TANGRAM__PSP_11__userName']")
element1.clear()
element1.send_keys('admin')
element1=element.find_element(By.XPATH,"//input[@id='TANGRAM__PSP_11__password']")
element1.clear()
element1.send_keys('123456')
sleep(1)
#登录弹出框输入内容
driver.find_element(By.XPATH,"//input[@id='TANGRAM__PSP_11__submit']").click()


##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器