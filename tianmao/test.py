import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import win32ui,win32con,pythoncom,win32gui,pyhooks

os.system('start chrome.exe --remote-debugging-port=9222')
# 获取浏览器控制器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 浏览器驱动
chrome_driver = r"C:\Users\PC\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


# 打开网址并获取信息
driver.get("https://www.alibaba.com/product-detail/Fashionable-Custom-Baby-Girl-Winter-Clothes_62435400195.html?spm=a2700.galleryofferlist.normal_offer.d_title.658f68e2JgdIpL")
print("标题：", driver.find_element(By.XPATH, "//div[@class='product-title']/h1").text)
print("销量：", driver.find_element(By.XPATH, "//div[@id='product-review']/div/span").text)

for i in range(4):
    if i > 0:
        print(driver.find_element(By.XPATH, "//div[@class='price-list']/div[%d]/div[1]" % i).text)
        print(driver.find_element(By.XPATH, "//div[@class='price-list']/div[%d]/div[2]" % i).text)

driver.quit()
