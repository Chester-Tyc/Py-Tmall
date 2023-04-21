import numpy as np
import pandas as pd
import openpyxl


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

df2 = pd.DataFrame(columns=columns)
df2 = df2._append(pd.DataFrame([[np.nan]*len(df2.columns)], columns=df2.columns), ignore_index=True)
df2 = df2._append(pd.DataFrame([[np.nan]*len(df2.columns)], columns=df2.columns), ignore_index=True)
'''df1.insert(0, '容量', '')
cap = ['128G', '256G', '512G', '1T']
for i in range(4):
    df1.iat[i, 0] = cap[i]'''

df1 = pd.read_excel(io='./竞品数据.xlsx')

df3 = pd.DataFrame()

print(df1)
print(df2)
print(df3)
frame = [df1, df1]
df = pd.concat(frame, axis=1)
print(df)
# df.to_excel('output.xlsx', index=False)
