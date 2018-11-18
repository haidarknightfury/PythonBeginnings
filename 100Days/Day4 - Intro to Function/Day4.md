## Functions

```py
    def factorial(num):
        result = 1
        for n in range(1,num+1):
            result*= n
        return result
```

### Default value in function parameter

```py
    def rollDice(n=2):
        total = 0
        for _ in range(n):
            total + = randint(1,6)
        return 0

    def total (a=0,b=0,c=0):
        return a + b + c
```

### Different number of arguments

```py
    def add(*args):
        total = 0
        for val in args:
            total + = val
        return total
```
- There is no method overload in python - i.e no two same methods can exist
- Can use two methods of same name provided they are in different modules

1. module1.py
```py
    def foo():
        print ('hello world')
```

2. module2.py
```py
    def foo():
        print('goodbye world')
```

3. test.py

```py
    from module1 import foo
    from module2 import foo
    
    # foo from module2 overwrites foo from module 1
    foo() # goodbye world
```


### __main__

1. __main__ is the name directly associated with the module being executed
2. if a module is being imported, then the executable code is going to be run 
3. Preferable to wrap execution code in if condition
4. when importing module3 below into another module, the execution of foo and bar wont happen

module3.py
```py
    def foo():
        pass
    
    def bar():
        pass
    
    if(__name__ == '__main__'):
        print ('Calling Foo')
        foo()
        print ('calling bar')
        bar()
```

### Variable Scope in Python

```py
    def foo():
    b = 300
    def bar():
        a = 300 
        print('a in bar is %d' %a) # a is 300 but, global variable a is unmodified
        print(b)
    bar()


if(__name__== '__main__'):
    a = 200
    foo()
    print('a in main is %d' % a) # a is still 200 and not modified
```

- To be able to modify global variables - use global keyword to access global variable
- The use of global scope should be limited in a python application - because it causes tight coupling

```py
    def foo():
        global a 
        a = 200
        print (a) # a is 200
    
    if (__name__ == '__main__):
        a = 300
        foo()
        print(a) # a is 200
```
