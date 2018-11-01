#  Enter two positive integers to calculate the greatest common divisor and the least common multiple

x = int(input('Enter x '))
y = int(input('Enter y '))

if(x > y):
    x, y = y, x
else:
    for factor in (x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('largest common divisor of %d and %d is %d' % (x, y, factor))
            print('least common multiple of %d and %d is %d' %
                  (x, y, x * y / factor))
            break
