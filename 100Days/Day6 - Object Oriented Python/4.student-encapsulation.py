# Setting private properties
class Student:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def study(self, subject):
        print('%s is studying %s' %(self.__name, subject))
    
    def __privateStudy(self):
        print('private method')
    
if __name__ == "__main__":
    stu = Student('haidar',22)
    # Can't access name or age property since private
    stu.study('Physics')
    print(stu._Student__name) # Hack to get to private member / do not use