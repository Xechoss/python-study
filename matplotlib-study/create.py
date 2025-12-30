import numpy as np
import matplotlib.pyplot as plt

# 折线图
x1 = np.linspace(-2 * np.pi, 2 * np.pi, 120)
y1, y2 = np.sin(x1), np.cos(x1)

# 创建画布
plt.figure(figsize=(8, 4), dpi=120)

# 单个折线
# llinestyle：折线的样式（例如：-表示实线，--表示虚线，:表示点线等）
# marker：数据点的标记（例如：*表示五角星）
# linewidth：折线的粗细
# plt.plot(x1, y1, linewidth=2, marker='*', color='red')
# 显示绘图
# plt.show()

# 多个折线
# plt.plot(x1, y2, linewidth=2, marker='>', color='blue')
# plt.show()

# 创建坐标系（第1个图）
plt.subplot(1, 2, 1)
plt.plot(x1, y1, linewidth=2, marker='*', color='red')
# 创建坐标系（第2个图）
plt.subplot(1, 2, 2)
plt.plot(x1, y2, linewidth=2, marker='^', color='blue')
# plt.show()

# 散点图
x2 = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
y2 = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])

plt.figure(figsize=(6, 4), dpi=120)
plt.scatter(x2, y2)
# plt.show()

# 柱状图
x20 = np.arange(4)
y20 = np.random.randint(20, 50, 4)
y21 = np.random.randint(10, 60, 4)
plt.figure(figsize=(6, 4), dpi=120)
# 通过横坐标的偏移，让两组数据对应的柱子分开，width：柱子粗细，label：柱子标签
plt.bar(x20 - 0.1, y20, width=0.2, label='A')
plt.bar(x20 + 0.1, y21, width=0.2, label='B')
# 横轴的刻度
plt.xticks(x20, labels=['Q1', 'Q2', 'Q3', 'Q4'])
# 定制显示图例
# plt.legend()
# plt.show()

labels = ['Q1', 'Q2', 'Q3', 'Q4']
plt.figure(figsize=(6, 4), dpi=120)
plt.bar(labels, y20, width=0.4, label='A')
# 注意：堆叠柱状图的关键是将之前的柱子作为新柱子的底部，可以通过bottom参数指定底部数据，新柱子绘制在底部数据之上
plt.bar(labels, y21, width=0.4, bottom=y21, label='B')
plt.legend(loc='lower right')
plt.show()
