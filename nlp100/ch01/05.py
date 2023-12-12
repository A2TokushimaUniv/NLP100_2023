def ngram(s, n):
    l = []
    for i in range(len(s)-n+1):
        l.append(s[i:i+n])
    return l
s = "I am an NLPer"
print(s)
print (ngram(s.split(),2))
print (ngram(s,2))
