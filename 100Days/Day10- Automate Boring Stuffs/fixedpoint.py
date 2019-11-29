def fixed_point(arr):
    for i in range(0,len(arr)):
        if i == arr[i]:
            return i
    return False

if __name__ == "__main__":
    res = fixed_point([-6, 0, 2, 40])
    print(res)
    res_2 = fixed_point([1, 5, 7, 8])
    print(res_2)
