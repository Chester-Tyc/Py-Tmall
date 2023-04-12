import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import numpy as np, pandas as pd
import xlwt, xlrd

os.system('start chrome.exe --remote-debugging-port=9222')
# 获取浏览器控制器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 浏览器驱动
chrome_driver = r"C:\Users\PC\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def jd():
    # 打开网址并获取信息
    driver.get(url1)
    num = range(5)
    # 获取商品价格
    for i in num:
        if i > 0:
            time.sleep(5)
            driver.find_element(By.XPATH, "//div[@id='choose-attr-2']/div[@class='dd']/div[%d]" % i).click()
            price = driver.find_element(By.XPATH, "//div[@class='dd']/span[1]").text
            print("容量：", driver.find_element(By.XPATH, "//div[@id='choose-attr-2']/div[@class='dd']/div[%d]" % i).get_attribute('title'))
            print("价格：", price)


def tmall(url):
    # 打开网站
    driver.get("https://detail.tmall.com/item.htm?id=%s" % url)
    time.sleep(5)
    # 尝试选择官方标配
    try:
        driver.find_element(By.XPATH, "//div[@class='skuCate'][4]/div[@class='skuItemWrapper']/div[@class='skuItem ']"
                                      "/div[@title='官方标配']").click()
    except NoSuchElementException:
        print("无法选择官方标配或已选择官方标配")
    # 定位价格模块
    capacity = driver.find_elements(By.XPATH, "//div[@class='skuCate'][2]/div[@class='skuItemWrapper']/div")
    # 循环点击各个容量
    for c in capacity:
        time.sleep(3)
        # 判断是否缺货
        if c.get_attribute('class') == 'skuItem disabled':
            print(c.text, '缺货')
            continue
        c.click()
        # 点击有库存的颜色
        driver.find_element(By.XPATH, "//div[@class='skuCate'][1]/div[@class='skuItemWrapper']/div[@class='skuItem ']").click()
        # 输出内存和价格
        price = driver.find_element(By.XPATH, "//div[@class='Price--extraPrice--2qsGsY3']").text
        print(c.text, price)
        # 重新点击当前颜色恢复原始状态，并在下一个循环重新选择内存
        driver.find_element(By.XPATH, "//div[@class='skuCate'][1]/div[@class='skuItemWrapper']"
                                      "/div[@class='skuItem current']").click()


url1 = "https://item.jd.com/100048731327.html#none"
url4 = "692178340554"
iPhone14pro = {'广东移动官方旗舰店': '688946628020', '喵速达': '688288232532', '中国移动手机官方旗舰店': '683384949809'}

# 店铺sku
product1 = {'广东移动官方旗舰店': '688946628020', '喵速达': '688288232532', '中国移动手机官方旗舰店': '683384949809'}
# 产品名单
productDict = {'iPhone14pro': product1}

# 循环调用函数输出对应商品的信息进excel
for p in productDict:
    # 输出商品名
    print(p)
    # 循环遍历该商品的所有店铺
    shop = productDict[p]
    for s in shop:
        print(s)
        tmall(shop[s])
        time.sleep(5)
driver.quit()

