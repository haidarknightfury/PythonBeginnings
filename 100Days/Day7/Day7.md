# Advanced Object Oriented 


1. Getters and Setters for properties

```py
    class Person(object):
        
        def __init__(self,name,age):
            self._name = name
            self._age = age
        
        @property
        def name(self):
            return self._name

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self,age):
            self._age = age
        
        @name.setter
        def age(self,name):
            self._name = name

        
```