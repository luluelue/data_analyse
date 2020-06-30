import numpy as np

arr1 = np.arange(64).reshape(8, 8)
arr2 = np.arange(64, 128).reshape(8, 8)

# 竖直拼接
print(np.vstack((arr1, arr2)))

# 水平拼接
print(np.hstack((arr1, arr2)))

# 第一行和第二行交换
arr1[[1, 2], :] = arr1[[2, 1],:]
print(arr1)

# 第二列和第一列交换
arr1[:,[1,2]] = arr1[:,[2,1]]
print(arr1)