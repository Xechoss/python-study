class Student:
    def __init__(self, score):
        self.score = score


class Student1:
    def get_score(self):
        return self._score

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score


class Student2:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score


if __name__ == '__main__':
    student = Student(60)
    student.score = 999
    print(student.score)

    student1 = Student1()
    student1.set_score(90)
    print(student1.get_score())
    # student1.set_score(999)  # ValueError: score must between 0 ~ 100!

    student2 = Student2()
    student2.score = 90
    print(student2.score)
    student2.score(999)
