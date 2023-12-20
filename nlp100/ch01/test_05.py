from typing import List

def to_bigram(array: List):
    # bigramは一つ前のお尻と一つあとの先頭はかぶるみたい
    bigram = [array[i:i+2] for i in range(len(array) - 1)]
    return bigram

def test_ngram():
    text = "I am an NLPer"

    result = {
        "word": to_bigram(text.split(" ")),
        "char": to_bigram(text),
    }

    assert result["word"] == [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    assert result["char"] == ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"]
