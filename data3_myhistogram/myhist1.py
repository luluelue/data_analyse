from matplotlib import pyplot as plt
import matplotlib

a = [5, 1, 8, 6, 5, 32, 8, 4, 7, 5, 6, 54, 2, 1, 54, 9, 85, 4, 14, 12, 23, 35, 4, 6, 68, 54, 26, 58, 67, 9, 4, 98, 25,
     45, 65, 23, 45, 67, 89, 47, 23, 12, 2, 8, 59, 53, 75, 41, 62, 9, 86]

d = 3

diff = max(a) - min(a)
num_bins = diff // d

print(diff)
print(num_bins)

plt.figure(figsize=(20, 8), dpi=100)

# 直方图，前面是数的集合，后面是组数
plt.hist(a, num_bins)

plt.xticks(range(min(a), max(a), d))

plt.plot()
plt.grid()

plt.show()
