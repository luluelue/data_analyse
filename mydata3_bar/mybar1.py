from matplotlib import pyplot as plt
import matplotlib

# ploty 画图工具，能够画出更加炫酷的图
# https://plotly.com/python/   有交互效果
font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 14
}
matplotlib.rc('font', **font)

plt.figure(figsize=(14, 15), dpi=100)
bar_width = 0.1

a = ["常见七号", "速度与激情7", "功夫熊猫", "变形金刚5", "最后的骑士", "加勒比海雕"]
b = [13, 88, 45, 34, 23, 67]
c = [5, 8, 69, 54, 12, 36]
x_b = range(len(b))
x_c = [i + bar_width for i in range(len(c))]

plt.bar(x_b, b, width=bar_width)
plt.bar(x_c, c, width=bar_width, color='red')
plt.xticks(x_b, a, rotation=45)

plt.plot()

# plt.savefig("../data_image/bar1.png")

plt.show()
