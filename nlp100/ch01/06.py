str1 = 'paraparaparadise'
str2 = 'paragraph'

def ngram(word,num):
    char1 = []
    for i in range(len(word)):
        char1.append(word[i:num+i])
    return char1
print('X:', ngram(str1, 2))
print('Y:', ngram(str2, 2))

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print('和集合: ', X | Y)
print('積集合: ', X & Y)
print('差集合: ', X - Y)

if 'se' in X:
    if 'se' in Y:
        print("XとYに'se'が含まれる")
    else:
        print("Xに'se'が含まれる")
else:
    if 'se' in Y:
        print("Yに'se'が含まれる")
    else:
        print("XとYに'se'が含まれない")