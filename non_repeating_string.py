#   WAP to print the first non repeating character in a string

def non_repeating(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in string:
        if freq[char] == 1:
            return char
    return None


print(non_repeating("Helle"))
