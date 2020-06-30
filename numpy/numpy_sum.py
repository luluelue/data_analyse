import numpy as np

arr = np.arange(64).reshape((8, 8)).astype(np.float)
arr[2, 3] = np.nan
arr[2, 4] = np.nan

# 打印出数组的形状，输出的是元组
print(arr.shape)

# 计算每行总和，axis=0，表示计算x轴,下面两种写法等价
print(np.sum(arr, axis=0))
print(arr.sum(axis=0))

# 计算y轴上的和
print(np.sum(arr, axis=1))

# 计算均值
print(np.mean(arr, axis=0))

# 计算中值
print(np.median(arr, axis=0))

# 计算最大值
print(np.max(arr, axis=0))

# 计算最小值
print(np.min(arr, axis=0))

# 计算机极值
print(np.ptp(arr, axis=0))

# 计算标准差
print(np.std(arr, axis=0))


# 将arr数组中的男值替换为均值
def fill_arr_nan(arr):
    # 根据列来遍历
    for i in range(arr.shape[1]):
        column = arr[:, i]
        # 下面这行可以统计出该列中nan的数目，因为false值即为0，故不为0 的值都是nan
        isNan = np.count_nonzero(column != column) > 0
        if isNan:
            # 当前列不为nan的array
            not_nan_cell = column[column == column]
            column[np.isnan(column)] = not_nan_cell.mean()
    return arr


print(fill_arr_nan(arr))
