from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """ Employee Abstract Class"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def getSalary(self):
        pass

class Manager(Employee):

    def getSalary(self):
        return 15000

class Programmer(Employee):
    def __init__(self, name, hours=0):
        super().__init__(name)
        self._hours = hours

    def getSalary(self):
        return self._hours * 1000

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = hours


if __name__ == '__main__':
    emps = [Manager('hd'), Programmer('hai', 10)]
    for emp in emps:
        if(isinstance(emp, Programmer)):
            print('Hello  Programmer %s' % emp.name)
        print(emp.getSalary())