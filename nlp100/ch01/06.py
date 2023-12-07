def ngram(s, n):
    l = []
    for i in range(len(s)-n+1):
        l.append(s[i:i+n])
    return l
s1 ="paraparaparadise"
s2 = "paragraph"
x = set(ngram(s1, 2))
y = set(ngram(s2, 2))
print(x | y)
print(x & y)
print(x - y)
print('se' in x)
print('se' in y)