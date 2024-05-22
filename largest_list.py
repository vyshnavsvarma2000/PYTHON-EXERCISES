a = [1, 2, 4, 5, 6, 7, 13, 18, 15]
largest = a[0]
second_largest = a[1]
for i in a:
    if i > largest:
        largest, second_largest = i, largest
    elif i > second_largest:
        second_largest = i
print("Largest element in the list is", largest)
print("Second largest element in the list is", second_largest)
