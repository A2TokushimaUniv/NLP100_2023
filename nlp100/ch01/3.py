sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split(" ")
len_list = []
for word in words:
    len_list.append(len(word))
print(len_list)
