import numpy as np
import pandas as pd


# 店铺sku
product1 = {'广东移动官方旗舰店': '688946628020', '喵速达': '688288232532', '中国移动手机官方旗舰店': '683384949809'}
product2 = {}
# 产品名单
productDict = {'iPhone14pro': product1}

index = []
columns = []

for p in productDict:
    index.append(p)

for s in product1:
    columns.append(s)

df = pd.DataFrame(index=range(10), columns=columns)
df.insert(0, '容量', '')
cap = ['128G', '256G', '512G', '1T']
for i in range(4):
    df.iat[i, 0] = cap[i]

print(df)



