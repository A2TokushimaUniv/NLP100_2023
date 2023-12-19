# 06. 集合Permalink
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(text, n):
    ngram = [] 
    for i in range(len(text) - n + 1):
        # ngram_ = text[i:i+n]
        ngram.append(text[i:i+n]) 
    return ngram

X_text = 'paraparaparadise'
Y_text = 'paragraph'

#「set()」を用いることで、集合の概念を扱える
X = set(n_gram(X_text, 2))
Y = set(n_gram(Y_text, 2))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)

if "se" in X:
    if "se" in Y:
        print("XとYに'se'が含まれる")
    else:
        print("Xに'se'が含まれる")
elif "se" in Y:
    print("Yに'se'が含まれる")
else:
    print("どちらにも含まれていない")