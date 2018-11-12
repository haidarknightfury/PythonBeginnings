import sys

def main():
    list1 = ['1', '2', '4', '3']
    list2 = sorted(list1)
    print(list2)

    # Sort reverse order
    list3 = sorted(list1, reverse=True)
    print(list3)

    # Sort by key
    list4 = sorted(list1, key=len)
    print(list4)

    # Apply sort on object
    list1.sort(reverse=True)
    print(list1)


def generateList():
    print('---------List Generation-------')
    f = [x for x in range(1, 20)]
    print(f)

    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    # This type of creation takes space
    f = [x**2 for x in range(1,1000)]
    print(f)
    print(sys.getsizeof(f))

    # Create generator object instead
    f = (x**2 for x in range(1,1000))
    print(sys.getsizeof(f))
    print(f)

    for val in f:
        print(val , end = ' ')




if __name__ == '__main__':
    main()
    generateList()
