# WAP to check the intersection of two arrays

def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9, 3]))
