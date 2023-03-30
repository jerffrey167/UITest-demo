from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://120.46.215.163:4000/user/login')
driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys("jsh")
driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys("123456")
driver.find_element(By.CSS_SELECTOR,'button[type]').click()
driver.find_element(By.CSS_SELECTOR,"a[role='button'][class='introjs-skipbutton']").click()
# 消除提示框
driver.find_element(By.XPATH,"//span[text()='销售管理']/..").click()
driver.find_element(By.XPATH,"//span[text()='销售订单']/..").click()

driver.find_element(By.XPATH,"//span[text()='新增']/..").click()
driver.find_element(By.CSS_SELECTOR,"a[class='introjs-skipbutton']").click()
# 消除提示框
driver.find_element(By.XPATH,"//div[text()='选择客户']/..").click()
driver.find_element(By.CSS_SELECTOR,"ul[role='listbox']>li:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"i[class='anticon anticon-search ant-input-search-icon']").click()
#弹出商品选择框
driver.find_element(By.CSS_SELECTOR,"input[placeholder='条码、名称、规格、型号、颜色']").send_keys("商品test1")
driver.find_element(By.XPATH,"//span[text()='新 增']/../..").click()
sleep(1)
driver.find_element(By.XPATH,"//*[@class='ant-modal']//descendant::input[4]").click()
#勾选按钮
driver.find_element(By.CSS_SELECTOR,"html button[type=button][class='ant-btn ant-btn-primary']:nth-child(2)").click()
#确定按钮
driver.find_element(By.CSS_SELECTOR,"input[id^='remark_jet']").send_keys("我新增第一条插入行的备注内容")
driver.find_element(By.XPATH,'//*[@placeholder="请输入备注"]').send_keys("我新增条目的备注内容")
driver.find_element(By.XPATH,'//input[@placeholder="请输入优惠率"]').send_keys("20")
driver.find_element(By.XPATH,'//input[@placeholder="请输入收取订金"]').send_keys("10")
driver.find_element(By.XPATH,"//span[text()='保 存']/..").click()
########## 新增完成
driver.find_element(By.XPATH,"//a[contains(text(),'展开')] ").click()
driver.find_element(By.XPATH,"//*[@title='客户']/../../div[2]/div/span/div").click()

driver.find_elements(By.XPATH,"ul[role='listbox'][tabindex='0']")
driver.find_element(By.XPATH,"//li[contains(text(),'客户3')]").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
sleep(22)



