class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        pass


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def sleep(self):
        print("student sleep")


class Teacher(Person):
    def sleep(self):
        print("teacher sleep")


class Boss(Person):
    def __init__(self, name, age, ultimate, hp):
        super().__init__(name, age)
        self._ultimate = ultimate  # 单下划线表示protected
        self.__hp = hp  # 双下划线表示private

    def get_hp(self):
        return self.__hp


def goto_sleep(person: Person):
    person.sleep()


if __name__ == '__main__':
    student = Student("张三", 18, 100)
    teacher = Teacher("李老师", 30)
    goto_sleep(student)
    goto_sleep(teacher)
    # goto_sleep("")

    boss = Boss('boss', 900, "ultimate", 1000)
    # print(boss.__hp)  # Unresolved attribute reference '__hp' for class 'Boss'
    boss.__hp = 10
    print(boss._ultimate)  # Access to a protected member _ultimate of a clas
    print(boss.__hp)  # 10
    print(boss.get_hp())  # 1000
