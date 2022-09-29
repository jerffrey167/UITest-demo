from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
商城购物流程
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://192.168.3.12:88/')
#浏览器打开商城网站
sleep(2)
driver.find_element(By.XPATH,"//a[text()='登录']").click()
sleep(1)
#进入登录页面
driver.find_element(By.XPATH,'//*[@id="loginAccount"]').send_keys('jerffrey')
driver.find_element(By.XPATH,'//*[@id="loginPassword"]').send_keys('12345678')
driver.find_element(By.XPATH,"//button[text()='会员登录']").click()
sleep(1)
###########账号登录  //div[@class='xm-goods-item']
driver.find_element(By.XPATH,"//a[text()='电视']").click()
sleep(1)


driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器