class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        print('%s is playing' % self._name)

# pass Person class into parameter
class Student(Person):
    def __init__(self, name, age, grade):
        # call superclass constructor
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self):
        print('%s is learning and grade is %d' % (self._name, self._grade))


class Teacher(Person):
    def __init__(self, name, age, title):
        # call superclass constructor
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def grade(self, title):
        self._title = title

    def teach(self):
        print('%s is teacher and title is %s' % (self._name, self._title))



if (__name__ == '__main__'):
    person=Person('haidar', 22)
    student = Student('baka', 23, 100)
    student.play()
    student.study()
    teacher =  Teacher('korosensei',90, 'asssassin')
    teacher.teach()
