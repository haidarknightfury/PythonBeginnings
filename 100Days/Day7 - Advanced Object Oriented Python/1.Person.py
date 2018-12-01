class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    # To string method
    def __str__(self):
        return ('%s has age %d' % (self._name, self._age))


def main():
    person = Person('haidar', 22)
    person.name = 'another' # Automatically applies the setter
    print(person)
    print(person.name) # Automatically gets the setter

if __name__ == '__main__':
    main()
