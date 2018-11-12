def main():
    t = ('hello', 'world', 38)
    print(t)

    # Accessing Index of Tuples
    print(t[0])
    print(t[2])

    for member in t:
        print(member, end = ' ')
    
    t = ('reassigning', 'to', 'a' , 'tuple')
    print(t)

    # Converting tuple to list
    person = list(t)
    print(person)
    person[0] = 'haidar'
    person[1] = 25
    print(person)

    # Convert list to tuple
    fruit_list = ['banana', 'grape', 'apple']
    fruit_tuple = tuple(fruit_list)
    print(fruit_tuple)


    # Tupples - thread safe - not mutable
    # Better than list in cration time and space
    # %timeit [1,2,3,4,5] -in ipython to know creation time



if __name__ == '__main__':
    main();