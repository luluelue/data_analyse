from matplotlib import pyplot as plt
import matplotlib

font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 14
}
matplotlib.rc('font', **font)

plt.figure(figsize=(14, 15), dpi=100)

a = ["常见七号", "速度与激情7", "功夫熊猫", "变形金刚5", "最后的骑士", "加勒比海雕"]
b = [13, 88, 45, 34, 23, 67]

plt.barh(range(len(a)), b, height=0.1,color ="cyan")
plt.yticks(range(len(a)), a, rotation=45)

plt.plot()
plt.grid()
# plt.savefig("../data_image/bar1.png")

plt.show()
