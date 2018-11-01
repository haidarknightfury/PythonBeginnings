sum = 0
for x in range(2, 102, 2):
    sum += x
print('Sum is %.1f' % sum)


sumy = 0
for y in range(1, 101):
    if(y % 2 == 0):
        sumy += y
print('Sum is %d' % sumy)
