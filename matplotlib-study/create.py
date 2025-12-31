import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # Show Chinese label
plt.rcParams['axes.unicode_minus'] = False  # These two lines need to be set manually

# 1、折线图
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

# 2、散点图
x2 = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
y2 = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])

plt.figure(figsize=(6, 4), dpi=120)
plt.scatter(x2, y2)
# plt.show()

# 3、柱状图
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
plt.bar(labels, y21, width=0.4, bottom=y20, label='B')
plt.legend(loc='lower right')
# plt.show()

# 4、饼图
data = np.random.randint(100, 500, 7)
labels = ['苹果', '香蕉', '桃子', '荔枝', '石榴', '山竹', '榴莲']

plt.figure(figsize=(5, 5), dpi=120)
plt.pie(
    data,
    # 自动显示百分比
    autopct='%.1f%%',
    # 饼图的半径
    radius=1,
    # 百分比到圆心的距离
    pctdistance=0.8,
    # 颜色（随机生成）
    colors=np.random.rand(7, 3),
    # 分离距离
    # explode=[0.05, 0, 0.1, 0, 0, 0, 0],
    # 阴影效果
    # shadow=True,
    # 字体属性
    textprops=dict(fontsize=8, color='black'),
    # 楔子属性（生成环状饼图的关键）
    wedgeprops=dict(linewidth=1, width=0.35),
    # 标签
    labels=labels
)
# 标题
plt.title('水果销售额占比')
plt.show()

# 5、直方图
heights = np.array([
    170, 163, 174, 164, 159, 168, 165, 171, 171, 167,
    165, 161, 175, 170, 174, 170, 174, 170, 173, 173,
    167, 169, 173, 153, 165, 169, 158, 166, 164, 173,
    162, 171, 173, 171, 165, 152, 163, 170, 171, 163,
    165, 166, 155, 155, 171, 161, 167, 172, 164, 155,
    168, 171, 173, 169, 165, 162, 168, 177, 174, 178,
    161, 180, 155, 155, 166, 175, 159, 169, 165, 174,
    175, 160, 152, 168, 164, 175, 168, 183, 166, 166,
    182, 174, 167, 168, 176, 170, 169, 173, 177, 168,
    172, 159, 173, 185, 161, 170, 170, 184, 171, 172
])

plt.figure(figsize=(6, 4), dpi=120)
# 绘制直方图
plt.hist(heights, bins=np.arange(145, 196, 5), color='darkcyan')
# 定制横轴标签
plt.xlabel('身高')
# 定制纵轴标签
plt.ylabel('概率密度')
plt.show()

# 6、箱线图
# 数组中有47个[0, 100)范围的随机数
data = np.random.randint(0, 100, 47)
# 向数组中添加三个可能是离群点的数据
data = np.append(data, 160)
data = np.append(data, 200)
data = np.append(data, -50)

plt.figure(figsize=(6, 4), dpi=120)
# whis参数的默认值是1.5，将其设置为3可以检测极端离群值，showmeans=True表示在图中标记均值的位置
plt.boxplot(data, whis=1.5, showmeans=True, notch=True)
# 定制纵轴的取值范围
plt.ylim([-100, 250])
# 定制横轴的刻度
plt.xticks([1], labels=['data'])
plt.show()

# 7、气泡图
income = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
outcome = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])
nums = np.array([5, 3, 10, 5, 12, 20, 8, 10])

# 通过scatter函数的s参数和c参数分别控制面积和颜色
plt.scatter(income, outcome, s=nums * 30, c=nums, cmap='Reds')
# 显示颜色条
plt.colorbar()
# 显示图表
plt.show()

# 8、面积图
plt.figure(figsize=(8, 4))
days = np.arange(7)
sleeping = [7, 8, 6, 6, 7, 8, 10]
eating = [2, 3, 2, 1, 2, 3, 2]
working = [7, 8, 7, 8, 6, 2, 3]
playing = [8, 5, 9, 9, 9, 11, 9]
# 绘制堆叠折线图
plt.stackplot(days, sleeping, eating, working, playing)
# 定制横轴刻度
plt.xticks(days, labels=[f'星期{x}' for x in '一二三四五六日'])
# 定制图例
plt.legend(['睡觉', '吃饭', '工作', '玩耍'], fontsize=10)
# 显示图表
plt.show()

# 9、雷达图
labels = np.array(['速度', '力量', '经验', '防守', '发球', '技术'])
# 马龙和水谷隼的数据
malong_values = np.array([93, 95, 98, 92, 96, 97])
shuigu_values = np.array([30, 40, 65, 80, 45, 60])
angles = np.linspace(0, 2 * np.pi, labels.size, endpoint=False)
# 多加一条数据让图形闭合
malong_values = np.append(malong_values, malong_values[0])
shuigu_values = np.append(shuigu_values, shuigu_values[0])
angles = np.append(angles, angles[0])
# 创建画布
plt.figure(figsize=(4, 4), dpi=120)
# 创建坐标系
ax = plt.subplot(projection='polar')
# 绘图和填充
plt.plot(angles, malong_values, color='r', linewidth=2, label='马龙')
plt.fill(angles, malong_values, color='r', alpha=0.3)
plt.plot(angles, shuigu_values, color='g', linewidth=2, label='水谷隼')
plt.fill(angles, shuigu_values, color='g', alpha=0.2)
# 显示图例
ax.legend()
# 显示图表
plt.show()

# 10、玫瑰图
group1 = np.random.randint(20, 50, 4)
group2 = np.random.randint(10, 60, 4)
x = np.array([f'A组-Q{i}' for i in range(1, 5)] + [f'B组-Q{i}' for i in range(1, 5)])
y = np.array(group1.tolist() + group2.tolist())
# 玫瑰花瓣的角度和宽度
theta = np.linspace(0, 2 * np.pi, x.size, endpoint=False)
width = 2 * np.pi / x.size
# 生成8种随机颜色
colors = np.random.rand(8, 3)
# 将柱状图投影到极坐标
ax = plt.subplot(projection='polar')
# 绘制柱状图
plt.bar(theta, y, width=width, color=colors, bottom=0)
# 设置网格
ax.set_thetagrids(theta * 180 / np.pi, x, fontsize=10)
# 显示图表
plt.show()
