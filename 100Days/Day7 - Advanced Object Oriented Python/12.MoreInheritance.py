
class Person:
    def __init__(self,name):
         self.name = name

    def __repr__(self):
        return repr((self.name))

class Student(Person):

    def __init__(self, name, college):
         super().__init__(name)
         self.college = college
    
    def __repr__(self):
        return ((super().__repr__()+ ' '+  self.college))

if __name__ == "__main__":
    person = Person('haidar')
    student = Student('haidar','baka')
    print(person)
    print(student)