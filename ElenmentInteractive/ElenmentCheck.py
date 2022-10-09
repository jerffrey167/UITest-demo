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
print('a的文本 is',a)
b = driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[1]").get_attribute("href")
print('b的href属性的值 is',b)
c = driver.find_element(By.XPATH,"//div[@id='s-top-left']/a[1]").location
print('c的坐标 is',c)
d = driver.find_element(By.XPATH,"//*[@id='kw']").is_displayed()
print('d的是否存在 is',d)
e = driver.find_element(By.XPATH,"//*[@id='kw']").is_enabled()
print('e的是否被点击 is',e)
f = driver.find_element(By.XPATH,"//*[@id='kw']").is_selected()
print('f的是否被选中 is',f)
sleep(2)

driver.quit()
#关闭浏览器