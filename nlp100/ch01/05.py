# 05. n-gramPermalink
# 与えられたシーケンス（文字列やリストなど）から
# n-gramを作る関数を作成せよ．この関数を用い，
# ”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

#何個ずらすかも指定
def n_gram(text, n):
    ngram = [] 
    for i in range(len(text) - n + 1):
        # ngram += text[i:i+n]
        ngram_ = text[i:i+n]
        ngram.append(ngram_) 
    return ngram
text1 = "I am an NLPer"
#↓単語
word = text1.split()
w_bigram = n_gram(word, 2)
#↓文字
m_bigram = n_gram(text1, 2)

print("単語bi-gram:", w_bigram)
print("文字bi-gram:", m_bigram)


# def generate_ngram(text, n):
#     ngrams = []
#     for i in range(len(text) - n + 1):
#         ngram = text[i:i+n]
#         ngrams.append(ngram)
#     return ngrams
# #単語bi-gram
# text = "I am an NLPer"
# words = text.split()
# word_bigrams = generate_ngram(words, 2)

# # 文字bi-gram
# char_bigrams = generate_ngram(text, 2)

# # 結果の出力
# print("単語bi-gram:", word_bigrams)
# print("文字bi-gram:", char_bigrams)