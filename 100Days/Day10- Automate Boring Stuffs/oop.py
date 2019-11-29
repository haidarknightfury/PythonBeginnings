class Person:

    personClassAttribute = 'person'

    def __init__(self,name):
        self._name = name
        self.__superprivate = 'baka'

    @property
    def name(self):
        return self._name

    def say_hello(self):
        print('hello from person')

    @staticmethod
    def beep():
        print('Beeeeeeeep')

    def __repr__(self):
        return "Name is {}".format(self._name)


class Student(Person):
    age = 20
    def __init__(self, name, classroom):
        super().__init__(name)
        self._classroom = classmethod

    def say_hello(self):
        print('overriden method from Person')

    @property
    def classroom(self):
        return self._classroom

    # Class method invoked without creating object
    # cannot access self, the class is obtained as argument
    @classmethod
    def new_student(cls, name):
        return cls(name, 'default_classroom')

if __name__ == "__main__":
    person = Person('haidar')
    student = Student('haidar', 4 )
    print(person._Person__superprivate)
    print(person)
    print(student.age)
    print(student.name)
    student.say_hello()
    print(Student.new_student('kirito kun'))
    Student.beep()
    print(Person.personClassAttribute)