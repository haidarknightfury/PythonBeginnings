import random
def numberGuesser():
    num = random.randint(1,10)
    num_input = int(input('Enter number'))
    while (num_input != num):
        num_input = int(input('Enter number'))
    print(f'you correctly guessed the number:  {num}')

if __name__ == "__main__":
    numberGuesser()