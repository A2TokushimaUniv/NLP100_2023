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


# 文字列の場合
## 文字bi-gramの生成
text = "I am an NLPer"
char_bigrams = generate_ngrams(text, 2, type="moji")
print("文字bi-gram:", char_bigrams)

## 単語bi-gramの生成
word_bigrams = generate_ngrams(text, 2, type="tango")
print("単語bi-gram:", word_bigrams)

# リストの場合
## 文字bi-gramの生成
text = ["I", "am", "an", "NLPer"]
char_bigrams = generate_ngrams(text, 2, type="moji")
print("文字bi-gram:", char_bigrams)

## 単語bi-gramの生成
word_bigrams = generate_ngrams(text, 2, type="tango")
print("単語bi-gram:", word_bigrams)
