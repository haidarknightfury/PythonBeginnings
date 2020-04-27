def has_duplicates(phrase):
    word_dict = {}
    words = phrase.split(' ')
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        else:
            word_dict[word] +=1
    return word_dict
    

if __name__ == "__main__":
    dc = has_duplicates('hello my name is haidar')
    print(dc)