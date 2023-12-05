sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sentence.split()

map = {}

for i, word in enumerate(words, 1):
    if i in[1, 5, 6, 7, 8, 9, 15, 16, 19]:
        map[word[0]] = i
    else:
        map[word[:2]] = i
print(map)