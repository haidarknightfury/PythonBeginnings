def is_progression(arr):
    prev = arr[0]
    cdiff = arr[1] - prev
    for i in range(2 ,len(arr)):
        ndiff = arr[i] - arr[i-1]
        if ndiff != cdiff:
            return False
    return True

if __name__ == "__main__":
    print(is_progression([1,3,4,7]))
