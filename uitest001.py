from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.find_element(By.ID,'kw').send_keys('selenium')
sleep(3)
driver.find_element(By.ID,'su').click()
sleep(3)
driver.close()
driver.quit()
