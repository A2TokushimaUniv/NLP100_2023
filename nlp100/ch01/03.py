sentence = "Now I need a drink, alocoholic of course, after the heavy lectures involving quantum mechanics"

sentence = sentence.replace(",","").replace(".","")

words = sentence.split()

word_lengths = [len(word) for word in words]

print(word_lengths)
