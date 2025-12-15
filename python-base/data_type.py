# 基本数据类型
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

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
