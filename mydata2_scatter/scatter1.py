from matplotlib import pyplot as plt
import matplotlib

font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 14
}
matplotlib.rc('font', **font)

y3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 18, 5, 15, 19, 21, 22, 22,
      24, 26, 29, 33]
y10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 21, 23, 17, 21, 22, 15, 11, 15, 5, 13, 17, 18, 10, 11, 14,
       12, 8, 9, 29, 5, 2]
plt.figure(figsize=(20, 10), dpi=100)

x3 = range(1, 35)
x10 = range(60, 94)

plt.scatter(x3, y3, label="3月份")
plt.scatter(x10, y10, label="10月份")
_x = list(x3) + list(x10)
_xtick_labels = ["2020.3.{}".format(i) for i in x3]
_xtick_labels += ["2020.10.{}".format(i) for i in x10]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)

plt.xlabel("时间")
plt.ylabel("温度")

plt.legend(loc=2)

plt.show()
