from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://www.baidu.com')
#浏览器打开百度
sleep(2)
a = driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[1]").text
print('a is',a)
b = driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[1]").get_attribute("href")
print('b is',b)
c = driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[1]").location
print('c is',c)
d = driver.find_element(By.XPATH,"//*[@id='kw']").is_displayed()
print('d is',d)
e = driver.find_element(By.XPATH,"//*[@id='kw']").is_enabled()
print('e is',e)
f = driver.find_element(By.XPATH,"//*[@id='kw']").is_selected()
print('f is',f)
sleep(2)

driver.quit()
#关闭浏览器