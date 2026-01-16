class Person:
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


def goto_sleep(person: Person):
    person.sleep()


if __name__ == '__main__':
    student = Student("张三", 18, 100)
    teacher = Teacher("李老师", 30)
    goto_sleep(student)
    goto_sleep(teacher)
    # goto_sleep("")
