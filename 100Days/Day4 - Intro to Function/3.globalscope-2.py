def foo():
    global a
    a = 200
    print(a)

if(__name__ == '__main__'):
    a = 300
    foo()
    print(a)