from math import sqrt

# pass object as parameter to show inheritance
# Triangle extends object
class Triangle(object):
    
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    # Use of static method
    @staticmethod
    def if_valid(a,b,c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

def main():
    print(Triangle.if_valid(1,2,3))
    triangle = Triangle(4,5,6)
    print(triangle.perimeter())

if __name__ == '__main__':
    main()
    

    
