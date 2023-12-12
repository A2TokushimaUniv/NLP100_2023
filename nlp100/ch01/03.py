s = "Now I need a drink, alcohol of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',', '')
s = s.replace('.', '')
l = []
for t in s.split():
    l.append([len(t)])