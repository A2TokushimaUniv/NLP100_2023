#“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def ngram(n, word):
    list = []
    for i in range(len(word) - n + 1):
        list.append(word[i:i+n])
    return list

text1 = "paraparaparadise"
text2 = "paragraph"

X = set(ngram(2, text1))
Y = set(ngram(2, text2))

print(f"和集合:{X | Y}")
print(f"積集合:{X & Y}")
print(f"差集合:{X - Y}")

if "se" in X:
    print("seはXに含まれる")
else:
    print("seはXに含まれない")

if "se" in Y:
    print("seはYに含まれる")
else:
    print("seはYに含まれない")