def match_words(words):
    count = 0
    lst = []
    for word in words:
        if len(word)>1 and word[0]== word[-1]:
            count+=1
            lst.append(word)

    print("list of words with first and last character same\n",lst)
    return count

print("number of words having first and last character same\n",match_words(['abc', 'cfc', 'xyz', 'aba', '1221']))        
    