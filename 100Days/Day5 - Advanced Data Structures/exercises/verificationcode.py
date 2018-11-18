import random


def generateCode(verificationlength=4):
    str = 'qwertyuiopasdfghjklzxcvbnm123456789'
    verification = ''
    for _ in range(0, verificationlength):
        verification = verification + str[random.randint(0,len(str) -1)]
    return verification


if __name__ == '__main__':
    verif = generateCode()
    print(verif)