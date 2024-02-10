# 451. Sort Characters By Frequency (Medium)
# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

s = "tree"

def frequencySort(string):

    hashmap = {}

    # build hashmap         Note: You can also use python's Counter() to complete the same task
    for i in string:
        if i not in hashmap:
            hashmap.update({i : 1})
        else:
            hashmap.update({i : (hashmap.get(i) + 1)})

    # you'll have something like this: {'t': 1, 'r': 1, 'e': 2}
    # now sort
    hashmap = reversed(dict(sorted(hashmap.items(), key=lambda item: item[1])).items())

    # now make string
    string = ''
    for char, cout in hashmap:
        string += char * cout

    # return type: string
    # return the string in the order of the most occuring letters
    return string


print(frequencySort(s))