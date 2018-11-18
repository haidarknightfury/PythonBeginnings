from math import pow


def palindrome(n):
    num = int(n)
    count = len(str(n)) - 1
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + rem * pow(10, count)
        count -= 1
        num = num // 10
    return sum == n

    
if (__name__ == '__main__'):
    num = int(input('Enter a number'))
    print(palindrome(num))