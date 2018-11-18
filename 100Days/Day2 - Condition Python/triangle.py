import math

# Determines whether the input side length can form a triangle.
# If it can, calculate the circumference and area of ​​the triangle.

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b > c and a+c > b  and b +c > a:
    print ('circumference %f'%(a+b+c))
    perimeter = (a+b+c)/2
    area = math.sqrt(perimeter*(perimeter -a)*(perimeter-b)*(perimeter-c))
    print('area %f' %(area))
else:
    print('Cannot form a triangle')
