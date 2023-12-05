def generate_ngram(sequence, n):

    ngram_set = set()
    for i in range(len(sequence) - n + 1):
        ngram = sequence[i:i + n]
        ngram_set.add(ngram)
    return ngram_set

text1 = "paraparaparadise"
text2 = "paragraph"

X = generate_ngram(text1, 2)
Y = generate_ngram(text2, 2)

union_set = X.union(Y)

intersection_set = X.intersection(Y)

difference_set = X.difference(Y)

se_in_X = 'se' in X
se_in_Y = 'se' in Y

print("X: ", X)
print("Y: ", Y)
print("wasyugou: ", union_set)
print("sekisyugou: ", intersection_set)
print("sasyugou(X - Y): ", difference_set)
print("'se' in X: ", se_in_X)
print("'se' in Y: ", se_in_Y)