# 基本数据类型
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# bool类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0

print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# 字符串
s = 'hello world'
print(s)
print(s[0])
print(s[0:-1])
print(s[6:])
print(s * 2)
print(s + '.')
print('hello\nworld')
# s[0] = 'H'  # TypeError: 'str' object does not support item assignment

# 列表
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('列表', l, type(l))
print(l[:5])
print(l[::2])
print(l[::-1])
l[0] = -1
print(l)

# 元组
t = (5, 'str', 1 + 3j)
print(t[1])
# t[0] = 1  # 'tuple' object does not support item assignment

# 集合
a = {1, 2, 3, 4, 5}
print("集合", a, type(a))
a = {1, 2, 3, 3, 3}
print("集合", a)

# 字典
d = {'a': 1, 'b': 2}
print("字典", d, type(d))
print("d['a']", d['a'])
