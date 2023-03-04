from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
百度登录框
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('https://www.baidu.com/')
#浏览器打开baidu网站
sleep(2)
driver.find_element(By.XPATH,'//*[@id="s-top-loginbtn"]').click()
#打开登录弹出框 
sleep(1)
# element=driver.find_element(By.XPATH,'//*[@id="passport-login-pop-api"]')
# element1=element.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys('1111')
# element2=element.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys('22222')
# element3=element.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()

#####################################switch to 方法
driver.switch_to.active_element.find_element(By.XPATH,'//*[@id="passport-login-pop-api"]')
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys('1111')
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys('22222')
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').clear()
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').clear()
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()

sleep(2)
########先进入层级，然后在层级中再寻找元素
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器