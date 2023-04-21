import math
import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import pandas as pd
import openpyxl
import math


os.system('start chrome.exe --remote-debugging-port=9222')
# 获取浏览器控制器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 浏览器驱动
chrome_driver = r"C:\Users\PC\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def jd():
    # 打开网址并获取信息
    driver.get("https://item.jd.com/100048731327.html#none")
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
    price_list = []
    # 循环点击各个容量
    for c in capacity:
        time.sleep(3)
        # 判断是否缺货
        if c.get_attribute('class') == 'skuItem disabled':
            print(c.text, '缺货')
            price_list.append('缺货')
            continue
        c.click()
        # 点击有库存的颜色
        driver.find_element(By.XPATH, "//div[@class='skuCate'][1]/div[@class='skuItemWrapper']/div[@class='skuItem ']").click()
        # 输出内存和价格
        price = driver.find_element(By.XPATH, "//div[@class='Price--extraPrice--2qsGsY3']").text
        print(c.text, price)
        price_list.append(price)
        # 重新点击当前颜色恢复原始状态，并在下一个循环重新选择内存
        driver.find_element(By.XPATH, "//div[@class='skuCate'][1]/div[@class='skuItemWrapper']"
                                      "/div[@class='skuItem current']").click()
    # 返回各店铺价格数组
    return price_list

#'中国联通官方旗舰店': '683984779835'
# 店铺sku
product1 = {'广东移动官方旗舰店': '688946628020', '喵速达': '683734682879', '中国移动手机官方旗舰店': '683384949809',
            }
product2 = {'广东移动官方旗舰店': '692178340554', '喵速达': '692388372567', '中国移动手机官方旗舰店': '702660784568',
            }
# 产品名单
productDict = {'iPhone14pro': product1, 'vivoX90': product2}


# 新建Dataframe存储价格数据
df1 = pd.read_excel(io='./竞品数据.xlsx')
columns = []
for s in product1:
    columns.append(s)
df2 = pd.DataFrame(columns=columns)


# 循环调用函数将对应商品的价格输入数组
for p in productDict:
    # 输出商品名
    print(p)
    # 新建一个Dataframe装载商品的所有店铺数据
    df3 = pd.DataFrame()
    # 循环遍历该商品的所有店铺
    shop = productDict[p]
    # 输出记录价格的二维数组
    for s in shop:
        # 输出店铺名
        print(s)
        # 获取当前店铺的价格数组并插入Dataframe中
        shop_price = tmall(shop[s])
        try:
            df3.insert(loc=len(df3.columns), column=s, value=shop_price)
        except ValueError:
            shop_price.append(math.nan)
            df3.insert(loc=len(df3.columns), column=s, value=shop_price)
        print(df3)
        time.sleep(5)
    # 将当前的店铺价格拼接上去
    df2 = pd.concat([df2, df3], axis=0, ignore_index=True)

frame = [df1, df2]
df_ = pd.concat(frame, axis=1)
print(df_)
df_.to_excel('output.xlsx', index=False)
driver.quit()
