# coding=utf-8
import random

import matplotlib
from matplotlib import pyplot as plt

# 设置打印图形的中文支持
font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 14
}
matplotlib.rc('font', **font)

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)

# 这里是将x转化为列表，再将列表隔10取1
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]

# 第一个参数是x轴的刻度，这里的第二个参数是标签,第三个标签是旋转的度数
plt.xticks(_x[::10], _xtick_labels[::10], rotation=90)

plt.show()
