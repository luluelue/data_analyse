import pandas as pd

# 创建一个series(series是一个索引列表，默认索引从0开始）也可以指定索引，即传入一个字典
series = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(series)

series1 = pd.Series({"name": "xiaolu", "age": 20, "tel": 10010})
print(series1)

# 取特定索引的值
print(series1[["name", "age"]])

# 获取series的标签
print(series1.index)
