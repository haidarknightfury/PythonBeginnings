# Class that manage abstract
# ABCMetametaclass - wrap in abstract class
# need to import abstract method to use abstract
# Pet class cannot be instantiated
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass= ABCMeta):
    """ pet abstract class"""

    def __init__(self, nickname):
        self._nickname = nickname
    
    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    """ Dog class extends Pet"""
    # No other attributes

    def make_voice(self):
        print('%s woof woof' %self._nickname)


class Cat(Pet):
    """ Cat class extends Pet"""
    # No other attributes

    def make_voice(self):
        print('%s meooooooow' % self._nickname)

if __name__ == '__main__':
    pets =[Dog('bob'), Cat('billy'), Dog('blacky')]
    for pet in pets:
        pet.make_voice()

    
    
