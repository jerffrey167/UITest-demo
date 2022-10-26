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
driver.find_element(By.ID,'kw').send_keys('id定位')
#ID定位搜索框输入 selenium
sleep(1)
driver.find_element(By.ID,'su').click()
#ID定位搜索按钮
sleep(2)
# 获取页面元素
element = driver.find_element(By.XPATH,"//*[@id='rs_new']/div")
# 移动元素element对象，与当前窗口的中心对齐
## 不需要增加括号
element.location_once_scrolled_into_view
sleep(2)
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器