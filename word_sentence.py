# WAP to fetch the count of occurence of a word from a given sentence

def occurence(sentences):
    words = sentences.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


print(occurence("the river flows , the sun shines "))
