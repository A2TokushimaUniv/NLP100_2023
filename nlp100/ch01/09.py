import random

def shuffle_words(sentence):
    words = sentence.split()
    shuffled_words = []

    for word in words:
        if len(word) > 4:
            # 長さが4より大きい場合は並び替え
            shuffled_word = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
        else:
            # 長さが4以下の場合は並び替えない
            shuffled_word = word

        shuffled_words.append(shuffled_word)

    return ' '.join(shuffled_words)

original_sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."

# 単語の並び替えを行う
shuffled_sentence = shuffle_words(original_sentence)

# 結果の表示
print("元の文:", original_sentence)
print("並び替え後:", shuffled_sentence)