import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(64).reshape(8, 8), index=list("aaaabbbb"), columns=list("poiuytre"))
print(df1)
# 分组统计数量
print(df1.groupby(by="e").count())
# 只取r列
print(df1.groupby(by="e").count()["r"])
# 取行并排序
print(df1.groupby(by="e").count().loc[15].sort_values(ascending=False))
