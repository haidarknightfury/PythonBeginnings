
def main():
    list = [1, 3, 5, 6, 7, 8, 100]
    print(list)

    list2 = ['Hello']
    print(list2 * 5)

    print(len(list))
    print(list[0])
    print(list[4])

    print(list[-1])
    print(list[-3])

    list[1] = 0
    print(list)

    list.append(200)
    list.insert(1,300)
    list += [100000,200000]
    print(list)

    if 100 in list:
        list.remove(100)
    del list[0]
    print(list)

    list.clear()
    print(list)

if __name__ == '__main__':
    main()
