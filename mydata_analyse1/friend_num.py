from matplotlib import pyplot as plt
import matplotlib

# 官网图形示例 https://matplotlib.org/gallery/index.html
# 设置打印图形的中文支持
font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 14
}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 8), dpi=120)

x = range(11, 30)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1]
y_2 = [1, 3, 1, 6, 0, 2, 1, 4, 2, 4, 4, 2, 3, 5, 4, 1, 6, 8, 2]

# 画出两条线
plt.plot(x, y_1, label="自己", color='cyan', linestyle=':')
plt.plot(x, y_2, label="BB", color='red', linestyle='dashed')

_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels)

# 设置网格线,(值表示不透明度）
plt.grid(0.9)

# 设置图例,参数loc为location，设置位置
plt.legend(loc=5)

plt.show()
