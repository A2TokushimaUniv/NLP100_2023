s1 = 'パトカー'
s2 = 'タクシー'
union = (''.join([a+b for a,b in zip(s1,s2)]))
print(union)