import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(72).reshape((8, 9)), columns=list("abcdefghi"))

# 将列表的某一列作为索引,drop=True 表示将a这列从原有列表中删掉（默认）
df2 = df1.set_index("a", drop=True)
# 复合索引
df3 = df1.set_index(["a", "b"], drop=False)

print(df2)
print(df3)
print(df2.index)

# 给某列去重操作(这里直接中括号取值，取的是列）
print(df1["e"].unique())
print(df1.loc[4])

# 复合索引取值
print(df3.loc[9].loc[10])

df1.loc[df1["a"] < 20, ["a"]] = "m"
df4 = df1.set_index(["a", "b"])
print(df4)
# 复合索引中取值,下面两种方法效果等同
print(df4.loc["m"].loc[10])
print(df4.loc["m",10])

# 交换索引
print(df4.swaplevel())
