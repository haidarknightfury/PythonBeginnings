from math import sqrt


def isPrime(n):
    root = int(sqrt(n))
    for div in range(2, root + 1):
        if n % div == 0:
            return False
    return True


if __name__ == '__main__':
    inp = int(input('Enter number'))
    print(isPrime(inp))
