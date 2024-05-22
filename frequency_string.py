# WAP to print the frequency of characters in a string


string = "Hello"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
