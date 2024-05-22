def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [1, 2, 3, 4]
x = 1
print(search(arr, x))
