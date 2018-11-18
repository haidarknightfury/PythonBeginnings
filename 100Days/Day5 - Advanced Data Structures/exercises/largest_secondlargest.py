# 1,2,3,4,5
def largest_secondlargest(arr):
    m1, m2 = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    for index in range(2, len(arr)):
        if arr[index] > m1:
            m2 = m1
            m1 = arr[index]
        elif arr[index] > m2:
            m2 = arr[index]
    return m1, m2


if __name__ == '__main__':
    l1, l2 = largest_secondlargest([1, 2, 3, 3, 4, 20, 20, 1, 18])
    print('%d | %d' % (l1, l2))
