s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',','').replace('.','')
[len(w) for w in s.split()]

print([len(w) for w in s.split()])