# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def generate_ngram(text, n):
    ngrams = set()
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        ngrams.add(ngram)
    return ngrams

# 文字列から文字bi-gramの集合を生成
X = generate_ngram("paraparaparadise", 2)
Y = generate_ngram("paragraph", 2)

# 和集合
union_set = X.union(Y)

# 積集合
intersection_set = X.intersection(Y)

# 差集合
difference_set = X.difference(Y)

# 'se'がXおよびYに含まれるかどうかの調査
se_in_X = 'se' in X
se_in_Y = 'se' in Y

# 結果の出力
print("X:", X)
print("Y:", Y)
print("和集合:", union_set)
print("積集合:", intersection_set)
print("差集合(X - Y):", difference_set)
print("'se' in X:", se_in_X)
print("'se' in Y:", se_in_Y)