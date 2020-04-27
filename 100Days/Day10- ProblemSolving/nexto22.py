def check22(arr):
    str_22 = "".join([str(x) for x in arr])
    return str_22.find('22') > -1

if __name__ == "__main__":
    res = check22([1,1,2,3,4,2])
    print(res)