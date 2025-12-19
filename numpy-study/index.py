import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
# 元素个数 5
print(array.size)
# 形状 (5,)
print(array.shape)
# 元素数据类型
print(array.dtype)

# 索引
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 和列表元组一样
print(array1)
print(array1[1])
print(array1[1][1])
print(array1[1, 1])
print(array1[-1][-1])

# 切片
print(array1[1, :2])
print(array1[::2, ::2])

print(array[[0, 2, 1, -1, -2]])
print(array1[[0, 2]])
print(array1[[0, 2], [1, 2]])

print(array[[True, True, False, False, True]])
print(array1 > 5)
