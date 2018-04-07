#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    fib = [];
    fib.append(0)
    fib.append(1)
    for i in range(n+1):
        if i > 1:
            fib.append(fib[i-1] + fib[i-2])
    return fib[len(fib) - 1]
