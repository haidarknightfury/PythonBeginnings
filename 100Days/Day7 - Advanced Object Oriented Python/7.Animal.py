from abc import ABCMeta , abstractmethod

class Animal(object, metaclass = ABCMeta):
    
    def __init__(self, type):
        self._type = type
    
    @abstractmethod
    def speak(self):
        pass

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type


class Mammal(Animal):

    def __init__(self, typ, hasfur):
        super().__init__(typ)
        self._hasfur = hasfur
    
    def speak(self):
        print(self.type)


if __name__ == "__main__":
    whale = Mammal('underwater',True)
    whale.speak()
