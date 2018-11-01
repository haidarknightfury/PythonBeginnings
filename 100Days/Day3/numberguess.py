import random

answer = random.randint(1,100)
count = 0

while True:
    count +=1
    number = int(input('Enter number'))
    if(number < answer):
        print('bigger')
    elif(number> answer):
        print('smaller')
    else:
        print('guessed right')
        break
print('you guessed a total of %d times' %count)
