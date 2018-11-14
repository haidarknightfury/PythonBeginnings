def main():
    scores = {'A': 95, 'B': 75}
    print(scores['A'])

    # Traversing
    for elem in scores:
        print(' %s -> %d' % (elem,  scores[elem]))

    #Updating map
    scores['c'] = 50
    scores ['d'] = 40
    print(scores)

    # Check if in dictionarry
    if 'd' in scores:
        print(scoregit s['d'])
    
    # Get + default value - if not present
    print(scores.get('e',30))

    #Removing items
    print(scores.popitem())

    #Remove but if not present default
    print(scores.pop('x',40))

    #Clear everything
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
