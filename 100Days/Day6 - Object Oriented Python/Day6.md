# Object Oriented Python

- A lot of static features (properties) and dynamic features (behaviors) of objects with common features, we can define something called a "class".
- Make a set of data structures and methods to process them into objects, 
- Classify objects of the same behavior into classes, 
- Hide internal details through class encapsulation, 
- And implement class specialization through inheritance ( Specialization) and generalization,
- The dynamic assignment based on object type through polymorphism.


1. Student Class
   
 ```py

    class Student(object):

        # Constructor, self refer to 'this'
        def __init__(self, name , age):
            self.name = name;
            self.age = age;

        # Methods , Self passed as parameter
        def study(self, course_name):
            print('%s is learning %s %(self.name, course_name))
    
    def main():
        student1 = Student('Haidar',22)
        student1.study('Maths')
        print(student1.name)

    if __name__ == '__main__':
        main();
 ``` 

2. Using encapsulation to hide attributes

```py
        class Student(object):

        # Constructor, self refer to 'this'
        def __init__(self, name , age):
            self.__name = name;
            self.__age = age;

        # Methods , Self passed as parameter
        def study(self, course_name):
            print('%s is learning %s %(self.__name, course_name))

        def __help():
            print('private method')
    
    def main():
        student1 = Student('Haidar',22)
        student1.study('Maths')
        print(student1.name)

    if __name__ == '__main__':
        main();

```


## Object oriented Pillars

- encapsulation, inheritance, and polymorphism
- hide all the implementation details that can be hidden, and only expose (provide) a simple programming interface to the outside world.
- only need to know the name of the method and the parameters passed in  without knowing the implementation details inside the method .