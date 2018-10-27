def fibonacci(n):
    current = 0
    next = 1
    for i in range (0,n):
        temp = next
        next = current + next
        current = temp
        #current,next = next, current+next
    return current

print(fibonacci(36))
