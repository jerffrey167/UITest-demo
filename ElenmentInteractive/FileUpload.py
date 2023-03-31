from  selenium import  webdriver
from  selenium.webdriver.common.by import By
from  time import  sleep
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('https://image.baidu.com/')
#浏览器打开考试系统
driver.implicitly_wait(6)
#隐式等待
driver.find_element(By.CSS_SELECTOR,'#sttb').click()
driver.find_element(By.CSS_SELECTOR,'input[type=file]').send_keys("C:\\Users\\jerffrey\\Pictures\\R-C.jpg")
sleep(5)

driver.quit()
#关闭浏览器