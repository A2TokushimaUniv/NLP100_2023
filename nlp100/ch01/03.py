
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word_lengths = [len(word.strip(",.")) for word in sentence.split()]

print(word_lengths)