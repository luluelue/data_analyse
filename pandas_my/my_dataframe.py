import pandas as pd
import numpy as np

# 创建一个dataframe,dataframe有行索引和列索引,
df = pd.DataFrame(np.arange(64).reshape((8, 8)))

# 创建一个指定索引的dataframe，indexs表示指定行索引，columns表示指定列索引
df_index = pd.DataFrame(np.arange(64).reshape((8, 8)), index=list("qwertyui"), columns=list("asdfghjk"))
print(df)
print(df_index)

# 下面这两种字典的类型都能生成同样的DataFrame,缺失的属性会被赋值NaN
dict1 = {"name": ["zhangsan", "lisi", "wangwu"], "age": [22, 23, 24], "tel": ["110", "120", "121"]}
dict2 = [{"name": "zhangsan", "age": 22, "tel": "110"}, {"name": "lisi",  "tel": "110"},
         {"name": "wangwu", "age": 24, "tel": "121"}]

df1 = pd.DataFrame(dict1)
print(df1)
df2 = pd.DataFrame(dict2)
print(df2)