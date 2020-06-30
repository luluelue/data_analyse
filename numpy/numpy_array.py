import numpy as np

t1 = np.arange(64)

print(t1)

print(t1.shape)

t3 = t1.reshape(4, 16)
print(t3)

# reshape 给数组重新定义形状
# print(t1.reshape((8, 8)))

# 展开
# print(t3.flatten())


print(t1.reshape(1, 64))
print(t1.reshape(64, 1))
