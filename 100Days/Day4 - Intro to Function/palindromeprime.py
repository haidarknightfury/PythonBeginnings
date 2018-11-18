from palindrome import palindrome
from prime import isPrime

def isPalindromeAndPrime(n):
    return palindrome(n) and isPrime(n)

if (__name__ == '__main__'):
    print(isPalindromeAndPrime(int(input('Enter Number'))))
