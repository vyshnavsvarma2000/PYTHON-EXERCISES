#Given a string, find the longest substring without repeating characters. sliding window

def longest_subset_without_repeating(s):
    left = 0
    char_set = set()
    max_len = 0
    for right in range(len(s)):
        if s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_subset_without_repeating("abcabbb"))
