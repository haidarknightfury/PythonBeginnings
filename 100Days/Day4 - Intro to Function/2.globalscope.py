def foo():
    b = 300
    def bar():
        a = 300
        print('a in bar is %d' %a)
        print(b)
    bar()


if(__name__== '__main__'):
    a = 200
    foo()
    print('a in main is %d' % a)

