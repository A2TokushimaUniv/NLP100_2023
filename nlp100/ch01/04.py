sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sentence = sentence.replace(".", "")

words = sentence.split()

word_map = {}

for i, word in enumerate(words, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        word_map[i] = word[0]      #hitomojimedake
    else:
        word_map[i] = word[:2]     #futamojimemade

print(word_map)