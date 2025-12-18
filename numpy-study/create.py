import numpy as np

array0 = np.array([1, 2, 3, 4, 5])
print(array0)

array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1)

array2 = np.arange(0, 20, 2)
print(array2)

array3 = np.arange(20, 0, -2)
print(array3)

# 等差数列
array4 = np.linspace(0, 12, 7)
print(array4)

# 等比数列
array5 = np.logspace(1, 10, num=10, base=2)
print(array5)

array6 = np.fromstring('1, 2, 3, 4, 5', sep=',', dtype='i8')
print(array6)


def fib(how_many):
    a, b = 0, 1
    for _ in range(how_many):
        a, b = b, a + b
        yield a


gen = fib(20)
print(gen)
array7 = np.fromiter(gen, dtype='i8')
print(array7)

# 10个[0,1)范围的随机小数
array8 = np.random.rand(10)
print(array8)

# 10个[1,100)范围的随机整数
array9 = np.random.randint(1, 100, 10)
print(array9)

# 正态分布随机数
array10 = np.random.normal(50, 10, 20)
print(array10)

# [0,1)范围的随机小数构成的3行4列的二维数组
array11 = np.random.rand(3, 4)
print(array11)

# [1,100)范围的随机整数构成的三维数组
array12 = np.random.randint(1, 100, (3, 4, 5))
print(array12)

array13 = np.zeros((3, 4))
print(array13)

array14 = np.ones((3, 4))
print(array14)

array15 = np.full((3, 4), 10)
print(array15)

array16 = np.eye(4)
print(array16)
