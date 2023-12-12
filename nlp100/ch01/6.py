# 5と同じ
def generate_ngrams(sentence, n, type="tango"):
    if type != "tango" and type != "moji":
        return
    # n-gram生成
    ngrams = []
    if type == "tango":
        # 単語bigramの場合はリストに変換
        if isinstance(sentence, str):
            sentence = sentence.split()
        elif not isinstance(sentence, list):
            return
    if type == "moji":
        # 文字bigramの場合はstrに変換
        if isinstance(sentence, list):
            sentence = " ".join(sentence)
        elif not isinstance(sentence, str):
            return

    for i in range(len(sentence) - n + 1):
        ngrams.append(tuple(sentence[i : i + n]))

    return ngrams


sentence1 = "paraparaparadise"
sentence2 = "paragraph"

x = set(generate_ngrams(sentence1, 2, "moji"))
print(x)
y = set(generate_ngrams(sentence2, 2, "moji"))
print(y)
# 和集合
print(x | y)
# 積集合
print(x & y)
# 差集合
print(x - y)
print(y - x)

se = ("s", "e")
if se in x:
    print("xに'se'が含まれています")
elif se in y:
    print("yに'se'が含まれています")
