n = int(input('enter number'))
sum = 0
for divisior in range(1, n, 1):
    if(n % divisior == 0):
        print(divisior, end=' ')
        sum += divisior
print()
if sum == n:
    print('%d is a perfect number' % n)