import numpy as np

# 形如 a=b[:] 的操作是视图的操作，a,和b的数据相互影响，修改a会影响到b

# 数组的切片
arr1 = np.arange(64).reshape(8, 8).astype(int)

print(arr1[1, :])
print(arr1[1])
# 取第二行(逗号前面表示行，后面表示列
print(arr1[2, :])

# 取第三行到后面的行
print(arr1[3:])
# 取第三行到第六行
print(arr1[3:6])

# 取不连续的多行(下面两种写法等同）
print(arr1[[2, 4, 6]])
print(arr1[[2, 4, 6], :])

# 取第一列
print(arr1[:, 1])

# 取连续多列
print(arr1[:, 2:])
print(arr1[:, [2, 5]])

# 取数组中单个值
print(arr1[2, 3])

# 取多行多列,取3-4行，3-5列
print(arr1[3:5, 3:6])

# 取多个不相邻的点(取出，（0,2）（1,3），（2,4） ）坐标点的位置
print(arr1[[0, 1, 2], [2, 3, 4]])
