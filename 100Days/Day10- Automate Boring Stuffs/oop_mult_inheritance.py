class Cat():
    def miaw(self):
        print('miaw')

class Dog():
    def wow(self):
        print('wow')

class HybridCatDog(Cat,Dog):
    def wowmiaw(self):
        self.miaw()
        self.wow()

if __name__ == "__main__":
    mi = HybridCatDog()
    mi.wowmiaw()