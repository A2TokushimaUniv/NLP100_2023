from typing import List
def to_bigram(array: List):
    # bigramは一つ前のお尻と一つあとの先頭はかぶるみたい
    bigram = [array[i:i+2] for i in range(len(array) - 1)]
    return bigram


def test_集合():
    text1 = "paraparaparadise"
    text2 = "paragraph"

    # setだと重複しない要素に変換され、集合演算が行えるようになる
    X = set(to_bigram(text1))
    Y = set(to_bigram(text2))

    results = {
        "union": X | Y,
        "intersection": X & Y,
        "difference": X - Y,
        "is_in_se_x": "se" in X,
        "is_in_se_y": "se" in Y
    }

    assert results == {
        "union": {'ar', 'pa', 'ra', 'di', 'ag', 'gr', 'ph', 'ad', 'is', 'ap', 'se'},
        "intersection": {'pa', 'ra', 'ap', 'ar'},
        "difference": {'ad', 'is', 'di', 'se'},
        "is_in_se_x": True,
        "is_in_se_y": False
    }
