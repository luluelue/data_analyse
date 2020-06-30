import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(36).reshape((9, 4)), columns=list("abcd"))
df2 = pd.DataFrame(np.arange(4).reshape((2, 2)), columns=list("ef"))
df3 = pd.DataFrame(np.arange(8).reshape((4, 2)), columns=list("af"))
print(df1)
print(df2)

# join按照行标签相同或者列标签相同进行合并操作
print(df1.join(df2))

# merge进行内连接，类似于mysql的内连接，当某个标签相同时，便可使用该标签进行内连接
print(df1.merge(df3, on="a"))


