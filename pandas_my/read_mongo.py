from pymongo import MongoClient
import pandas as pd

client = MongoClient()
collection = client["sungv"]["item"]
data = list(collection.find({}, {"content": 0}).limit(5))

print(data)

# 读入series
print(pd.Series(data[0]))

# 读入dataframe
df1 = pd.DataFrame(data)
print(df1)

# 下面是获取dataframe的一些信息
print(df1.index)
print(df1.values)
print(df1.shape)
print(df1.dtypes)
print(df1.info())


