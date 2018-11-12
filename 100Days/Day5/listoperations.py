def main():
    fruits = ['a','b','c','d']
    fruits += ['e','f']

    # Looping over array
    for fruit in fruits:
        print(fruit, end= ' ')
    
    # Slicing array
    fruits2 = fruits[1:4]
    print(fruits2)

    # Copy Array without references
    fruits3 = fruits[:]
    print(fruits3)

    # Copy from inverse
    fruits4 =  fruits[-1:-3]
    print(fruits4)

    # Reverse list
    fruits5 = fruits[::-1]
    print(fruits5)

if __name__ == '__main__':
    main()
