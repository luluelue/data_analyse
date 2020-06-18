# coding=utf-8
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14, 5.5, 48, 75, 63, 21, 78, 12, 65, 3]
# 设置图片大小,下面的设置的像素是 6000*2400
plt.figure(figsize=(15, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度
# plt.xticks(range(2, 100))
# 用列表推导式设置x轴刻度
_xtick_labels = [i / 2 for i in range(4, 75)]
plt.xticks(_xtick_labels[::3]) # 设置步长为 3/2 ，这里的3是传递给上面列表推导式的参数的i

# 设置y轴刻度
plt.yticks(range(2,100,5))



# 保存图片
# plt.savefig("../data_image/img1.png")

# 展示
plt.show()
