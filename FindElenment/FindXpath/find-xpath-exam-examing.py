from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('http://120.46.215.163:8102/#/login')
#浏览器打开考试系统
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('s2')
#用户名
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('123456')
#密码
driver.find_element(By.XPATH,'//button[@type="button"]').click()
#登录按钮
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 20px')]/span[text()='在线考试']").click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="screenfull"]/*[@class="svg-icon"]').click()
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 40px')]/span[text()='在线考试']").click()
sleep(1)
#点击在线考试页面
driver.find_element(By.XPATH,'//input[@placeholder="搜索考试名称"]').send_keys('演示考试')
sleep(1)
driver.find_element(By.XPATH,"//span[text()='去考试']").click()
#点击去考试按钮
sleep(1)
driver.find_element(By.XPATH,"//*[text()=' 开始考试 ']").click()
#点击开始考试按钮
sleep(3)
########
#单选题
#######
driver.find_element(By.XPATH,"//*[contains(text(),'A.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第一题 选A
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'B.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第二题 选B
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'C.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第三题 选C
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'D.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第四题 选D
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'A.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第五题 选A
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'B.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第六题 选B
#######
#多选题
#######
sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(),'A.')]//..").click()
driver.find_element(By.XPATH,"//*[contains(text(),'B.')]//..").click()
driver.find_element(By.XPATH,"//*[contains(text(),'C.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第七题 选A B C
sleep(1)
driver.find_element(By.XPATH,"//*[contains(text(),'B.')]//..").click()
driver.find_element(By.XPATH,"//*[contains(text(),'C.')]//..").click()
driver.find_element(By.XPATH,"//*[contains(text(),'D.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第八题 选B C D
#######
#判断题
#######
sleep(1)
driver.find_element(By.XPATH,"//*[contains(text(),'A.')]//..").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 下一题 ']//..").click()
#第九题 选A
sleep(1)
driver.find_element(By.XPATH,"//*[contains(text(),'B.')]//..").click()
#第十题 选B
##################################交卷
sleep(1)
driver.find_element(By.XPATH,"//span[text()=' 交卷 ']//..").click()
sleep(1)
# element=driver.find_element(By.XPATH,"//*[@aria-label='提示']/div")
# element1=element.find_element(By.XPATH,"//*[@aria-label='提示']//button[2]").click()
driver.find_element(By.XPATH,"//*[@aria-label='提示']//button[2]").click()
sleep(1)
################################账号注销
driver.find_element(By.XPATH,"//div[text()=' 学员2 ']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='退出登录']//..").click()
##################
driver.close()
#关闭浏览器器进程
driver.quit()
#关闭浏览器