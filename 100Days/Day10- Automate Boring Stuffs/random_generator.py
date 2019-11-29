import random
import sys

def getRandom():
    return random.randint(1, 10)

def earlyExit():
    while (True):
        response = input()
        if response == 'exit':
            sys.exit()
        print(f"you typed {response}")

if __name__ == "__main__":
    print(f"random is {getRandom()}")
    earlyExit()