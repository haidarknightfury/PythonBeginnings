def gcd(a, b):
    (a, b) = (b, a) if a > b else (a, b)
    for factor in range (a,0,-1):
        if(a%factor ==0) and (b%factor ==0):
            return factor

def lcm(a,b):
    return a*b // gcd(a,b)


if (__name__ == '__main__'):
    print(gcd(20,30))
