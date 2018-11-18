for i in range(1, 6):
    for x in range(1, i + 1):
        print('*',  end=' ')
    print()

N = 5
for row in range(0, N):
    for space in range(0, N - row):
        print(' ', end=' ')
    for star in range(0, row + 1, 1):
        print('*', end=' ')
    print()
