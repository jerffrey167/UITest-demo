from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
'''
考试系统的登录+输入框的条件查询+下拉框的条件查询+账号退出
'''
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('https://mail.163.com/')
sleep(2)
iframe = driver.find_element(By.XPATH,'//*[@frameborder="0"]')
driver.switch_to.frame(iframe)

#############切换到对应的iframe中
driver.find_element(By.XPATH,'//*[@name="email"]').send_keys('username')

driver.find_element(By.XPATH,'//*[@name="password"]').send_keys('userpasswd')
sleep(2)
driver.find_element(By.XPATH,'//*[@name="email"]').clear()
driver.find_element(By.XPATH,'//*[@name="password"]').clear()

driver.switch_to.default_content()
###############切换回主干页面
driver.find_element(By.XPATH,"//a[text()='企业邮箱']").click()

sleep(2)

driver.switch_to.window(driver.window_handles[0])
#切换浏览器窗口 0 是第一个窗口
sleep(2)




