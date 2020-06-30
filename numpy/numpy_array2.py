import random

import numpy as np

t1 = np.arange(64)

t2 = t1.reshape(4, 16)

t3_1 = np.arange(24).reshape(2, 3, 4)

# 从末尾开始，若维度重合即可计算(不同维度也可运算）
# 同纬度，在任意一维度重合，只要其他维度均为1，即可计算
t3_2 = t3_1 - np.arange(1, 4).reshape(1, 3, 1)
print(t3_1, "-", np.arange(1, 4).reshape(1, 3, 1))
print(t3_2)

t2_1 = np.arange(1, 5).reshape(4, 1)

# print(t2_1)
# print(t2-t2_1)

print(random.randint(1,10))
