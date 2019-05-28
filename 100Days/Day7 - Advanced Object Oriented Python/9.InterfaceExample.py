
class Class1():
    def run(self):
        print('class 1 running')

class Class2():
    def run(self):
        print('class 2 running')

if __name__ == "__main__":
    class1 = Class1()
    class2 = Class2()
    allclasses = [class1,class2]
    for c in allclasses:
        c.run()