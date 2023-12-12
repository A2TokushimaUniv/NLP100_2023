def word_bi_gram(t):
    w = t.split()
    bi_gram = [[w[i],w[i+1]] for i in range(0,len(w)-1)]
    return bi_gram

def str_bi_gram(t):
    bi_gram = [[t[i],t[i+1]] for i in range(0,len(t)-1)]
    return bi_gram

t= "I am an NLPer"
print(word_bi_gram(t))
print(str_bi_gram(t))