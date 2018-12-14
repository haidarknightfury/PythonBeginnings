def powers(n):
    base = n
    yield base
    while True:
        n = base * n
        yield n


if __name__ == "__main__":
    powergenerator = powers(3)
    number = int(input('Enter number'))
    for _ in range(0, number):
        print(next(powergenerator))


    