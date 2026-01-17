from functools import reduce


def square(x: int):
    return x * x


def add(x: int, y: int):
    return x + y


def add2(x: int, y: int, z: int):
    return x + y + z


def even_number(x: int):
    return x % 2 == 0


square_list = map(square, range(10))
print(square_list)
print(list(square_list))

print(list(map(str, range(10))))

print(reduce(add, range(10)))

# print(reduce(add2, range(10)))  # 只能接收两个参数

print(list(filter(even_number, range(10))))

print(sorted([-10, 2, -3, 16]))
print(sorted([-10, 2, -3, 16], reverse=True))
print(sorted([-10, 2, -3, 16], key=abs))

print(list(map(lambda x: x ** 2, range(10))))
