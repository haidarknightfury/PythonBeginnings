class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is studying %s' % (self.name, course_name))


def main():
    student1 = Student('Haidar', 22)
    student1.study('Maths')
    print(student1.name) # Name is not hidden


if __name__ == "__main__":
    main()
