# Hash-Table-Implementation.
# Give a string print a word frequency K.
def hashtable(string, k):
    hashm = {}
    for char in string:
        if char in hashm:
            hashm[char] += 1
        else:
            hashm[char] = 1
    chars = []
    for char in hashm:
        if hashm[char] == k:
            chars.append(char)
    return chars


s = "abcdefga"
k = 2
print(hashtable(s, k))
