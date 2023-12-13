#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．


def ngram(n, word):
    list = []
    for i in range(len(word) - n + 1):
        list.append(word[i:i+n])
    return list

sentence = "I am an NLPer"

print(f"単語bi-gram:{ngram(2, sentence.split())}")
print(f"文字bi-gram:{ngram(2, sentence)}")
