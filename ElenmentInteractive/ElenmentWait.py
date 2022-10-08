from  selenium.webdriver.support.wait import WebDriverWait
from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.implicitly_wait(10)

driver.find_element(By.ID,'kw').send_keys('python')

driver.find_element(By.ID,'su').click()

# 设置等待6秒，等待浏览器标题为python_百度搜索，结束等待，继续运行；
WebDriverWait(driver,6,1).until(lambda x:x.find_element(By.XPATH,'//*[@id="4"]'),message='元素查找失败')

driver.find_element(By.XPATH,'//*[@id="4"]//a[@data-click]').click()

sleep(2)

driver.quit()