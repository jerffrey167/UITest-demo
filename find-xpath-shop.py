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
driver.get('http://192.168.3.12:88/')
#浏览器打开百度
sleep(1)
driver.find_element(By.XPATH,'//a[text()="登录"]').click()
sleep(1)
#点击弹出登录弹出框
#element=driver.find_element(By.XPATH,"//div[@class='tang-content']")
driver.find_element(By.XPATH,'//*[@id="loginAccount"]').send_keys('jerffrey')
driver.find_element(By.XPATH,'//*[@id="loginPassword"]').send_keys('12345678')
driver.find_element(By.XPATH,'//*[text()="会员登录"and@type]').click()
sleep(2)
#登录弹出框输入内容
driver.find_element(By.XPATH,"//img[@alt='小米（MI）电视4A标准版 L55M5-AZ/L55M5-AD 55英寸']").click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="add_cart_submit"]').click()
##加入购物车
driver.find_element(By.XPATH,"//input[@name='keywords']").send_keys('家')
driver.find_element(By.XPATH,"//input[@class='search-btn iconfont']").click()
####搜索栏搜索
driver.find_element(By.XPATH,"//img[contains(text(),'西门子')]").click()
driver.find_element(By.XPATH,'//*[@id="add_cart_submit"]').click()
sleep(1)
#########添加购物车
driver.find_element(By.XPATH,'//*[@id="J_miniCart"]').click()
driver.find_element(By.XPATH,'//*[text()="去结算"]').click()
sleep(1)
driver.find_element(By.XPATH,'//*[text()="商家配送"]').click()


driver.find_element(By.XPATH,'//*[text()="退出"]').click()
################## //img[starts-with(@alt,'西门子（SIEMENS）')]
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器