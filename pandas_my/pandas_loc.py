import pandas as pd
from pymongo import MongoClient
import numpy as np

df1 = pd.DataFrame(np.arange(64).reshape((8, 8)), index=list("qwertyui"), columns=list("asdfghjk"))
print(df1)

# 下面是通过 标签 进行DataFrame的切片操作

# 根据行列标签得到值
print(df1.loc["w", "d"])
# 取行标签为w的行
print(df1.loc[["w"], :])
# 取列标签为d的列
print(df1.loc[:, ["d"]])

# 取行标签为q，w的行
print(df1.loc[["q", "w"], :])
# 取多行多列交叉值
print(df1.loc[["q", "w"], ["a", "d"]])

# 下面是通过 位置 进行的dataFrame的切片操作

print(df1.iloc[1, :])
print(df1.iloc[:, [1, 2]])
print(df1.iloc[[0, 1], [3, 4]])
# 取第一行后面的所有行，第二列前面的所有列
print(df1.iloc[1:, :2])

# 使用比较运算符来选择,注意两个条件之间需要使用括号括起来
print(df1[(df1["s"] > 20) & (df1["s"] < 50)])
