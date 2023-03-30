from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()
#浏览器窗口最大化
driver.get('https://cn.bing.com/')
#浏览器打开必应
sleep(1)
driver.find_element(By.ID,'sb_form_q').send_keys('翻译')
#ID定位搜索框输入 翻译
sleep(1)
driver.find_element(By.ID,'search_icon').click()
#ID定位搜索按钮
sleep(1)
#########
item = driver.find_element(By.XPATH,'//*[@id="tta_srcsl"]').click()
#点击打开下拉框
item = Select(driver.find_element(By.XPATH,'//*[@id="tta_srcsl"]'))
#获取下拉框选项
item.select_by_index(3)
# 选择下拉框的第3个内容
sleep(2)
item.select_by_value('zh-Hans')
#选择 value 为  zh-Hans 的选项
sleep(2)
item.select_by_visible_text('丹麦语')
sleep(2)

# driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]').send_keys('面板')
#############################################################################
sleep(1)

driver.find_element(By.XPATH,'//*[@aria-label="按照 时间不限 筛选"]').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="date_range_start"]').clear()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="date_range_start"]').send_keys("2023/2/4")
sleep(1)
driver.find_element(By.XPATH,'//*[@id="date_range_start"]').click()

sleep(1)

# driver.find_element(By.XPATH,'//*[@id="time_filter_done_link"]').click()

sleep(3)


driver.quit()
#关闭浏览器