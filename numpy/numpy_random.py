import numpy as np

arr = np.arange(64).reshape(8, 8)

# 生成一个二维的单列全0的数组,下面两行相同
zero_data = np.zeros((len(arr[0]), 1))
zero_data = np.zeros((arr.shape[0], 1))

# 生成一个二维的单列全1的数组
one_data = np.ones((len(arr[0]), 1))

# 创建一个全0的数组
zero_arr = np.zeros((8, 8))

# 创建一个对角线全1 的方阵
print(np.eye(8))

# 获取数组中最大值位置
print(np.argmax(arr))

# 获取数组中最小值位置
print(np.argmin(arr))

# 创建一个随机整数数组，1-20是其范围
print(np.random.randint(1, 20, (8, 8)))

# 创建一个维度为8*8 的标准正态分布随机数组
print(np.random.randn(8, 8))

# 创建一个8*8 的随机均匀分布的数组，值在0-1之间
print(np.random.rand(8, 8))

# 创建一个值在1-20之间的8*8的均匀分布数组
print(np.random.uniform(1, 20, (8 * 8)))

# 使用随机数种子来生成随机数
np.random.seed(100)
print(np.random.randint(1, 30, (5, 6)))


