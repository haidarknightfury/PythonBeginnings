class Animal:

    def __init__(self,category):
        self.category = category

    @staticmethod
    def say_type():
        print('ANIMAL')

class Dog(Animal):
    def __init__(self, name):
        super().__init__('DOG')
        self.__name = name

if __name__ == "__main__":
    dog = Dog('baka yaro')
    Animal.say_type()
    Dog.say_type()
    dog.say_type()

    