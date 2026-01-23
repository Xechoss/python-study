from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    # Mon = 2  # 运行会报错
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def main():
    print("月份")
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    print("星期")
    print(Weekday.Sun)

    print(Weekday['Mon'])

    print(Weekday.Sun.value)

    print(Weekday(1))  # 有相同的会选第一个


if __name__ == '__main__':
    main()
