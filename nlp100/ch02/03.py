import re
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = re.sub("[.,]", "", text)
print(text)
w = text.split(" ")
n = [len(i) for i in w]
print(n)