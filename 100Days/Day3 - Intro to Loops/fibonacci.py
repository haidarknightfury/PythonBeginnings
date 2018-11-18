# 0,1,1,2,3,5,8,13

n = int(input('Enter number'))
current = 0
next = 1
for i in range(1,n):
    sum = current + next
    current = next
    next = sum
print('Fibonnacci is %d' %current)
