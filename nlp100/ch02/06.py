def n_gram(n, t):
    n_gram = [t[i:i+n] for i in range(0,len(t)-n+1)]
    return n_gram

w1 = "paraparaparadise"
w2 = "paragraph"
bi_gram1 = n_gram(2,w1)
bi_gram2 = n_gram(2,w2)
X = set(bi_gram1)
Y = set(bi_gram2)
print("集合X： ",X)
print("集合Y： ",Y)
print("和集合： ",X|Y)
print("積集合： ",X&Y)
print("差集合： ",X-Y)
print("seが含まれているか: ", "se" in X|Y)