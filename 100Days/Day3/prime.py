from math import sqrt

n = int(input('enter number : '))
isPrime = True
root = int(sqrt(n))
for i in range(2, root + 1):
    if n % i == 0:
        isPrime = False
        break
if (isPrime == True):
    print('%d is a prime number' % n)
else:
    print('%d is not a prime number' % n)
