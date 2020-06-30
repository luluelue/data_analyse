import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(64).reshape(8, 8))
print(df1)

df1.iloc[[3, 4, 5], [2]] = np.nan
print(df1)

# 判断不为nan的数
print(pd.notnull(df1))
# 判断为nan的数
print(pd.isnull(df1))

# 删除含有nan的行,any 表示行含有 nan 即删除
print(df1.dropna(axis=0, how="any"))

# 删除含有nan的列，
print(df1.dropna(axis=1, how="any"))

# 删除行内所有元素都为nan的行
print(df1.dropna(axis=0, how="all"))

# 填充nan元素数据，这里将nan的单元格填充为0
print(df1.fillna(0))

# 填充nan元素数据，这里将nan的单元格填充为均值
print(df1.fillna(df1.mean()))



