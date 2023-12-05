s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',','').replace('.','')
#確認用
print(s)
print([len(w) for w in s.split()])