from math import sqrt, pow


class Point():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def moveTo(self, x, y):
        self._x = x
        self._y = y

    def moveBy(self, dx, dy):
        self._x = self._x + dx
        self._y = self._y + dy

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return('%d, %d' % (self._x, self._y))


def main():
    p1 = Point(0, 0)
    p2 = Point(2, 3)
    p2.moveBy(1,1)
    print(p1)
    print(p2)
    print(p1.distance_to(p2))
w
if __name__ == "__main__":
    main()