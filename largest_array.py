# WAP to find the largest element in an array

def array_largest(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest


print(array_largest([1, 13, 4, 15, 6]))
