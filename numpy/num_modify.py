import numpy as np

arr = np.arange(64).reshape(8, 8)

# 将第二行到第四行赋值为0
arr[2:4, :] = 0
print(arr)

# 打印出布尔索引
print(arr > 30)

arr = np.arange(64).reshape(8, 8)

# 将数组中为true的位置赋值
arr[arr < 5] = 10000
print(arr)

# where运算符,类似于三元运算符，将小于20的数替换为1，否则替换为100
print(np.where(arr < 20, 1, 100))

# 小于20的会被替换为20，大于50的会被替换成50
print(arr.clip(20,50))

# 转置,以下三种方法都是转置
arr_trans = arr.transpose()
arr_trans1 = arr.T
arr_trans2 = arr.swapaxes(1,0)
print(arr_trans)
print(arr_trans1)
print(arr_trans2)
