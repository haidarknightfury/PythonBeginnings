def main():

    # Defining a set - Duplicates are not entered   
    set1 = {1,2,3,4,5,4,2,1}
    print(set1)
    print(len(set1))

    #Constructing a set dynamically
    set2 =  set(range(1,10))
    print(set2)


    # Adding to a set
    set2.add(20)
    set2.add(21)
    print(set2)

    # Updating a set
    set2.update([30,31])
    print(set2)

    #Removing an element from set
    set2.discard(20)

    #Checking an element in set then remove - remove element must be in set
    if 4 in set2:
        set2.remove(4)

    # Looping a set
    for elem in set2:
        print(elem ** 2, end = ' ')

    #Converting a tuple to a set
    set3 = set((1,2,3,4,4,5,5,6))
    print(set3)

    #Pop Element in set
    print(set3.pop())


    #Intersection of sets
    print(set1 & set2)

    # Union
    print(set1 | set2)

    # Difference of sets
    print(set2 - set1)

    # Symettrice Difference
    print(set2.symmetric_difference(set1))
    print(set2^set1)

    # Subset
    print(set3 <= set1)

    # Superset
    print(set3 >= set1)

    # Disjoint
    print(set3.isdisjoint(set1))












if __name__ == '__main__':
    main()