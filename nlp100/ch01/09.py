# 09. TypoglycemiaPermalink
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文
# （例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
# その実行結果を確認せよ．

import random

def shuffle_word(word):
    if len(word) <= 4:
        return word
    else:
        first_char = word[0]
        last_char = word[-1] #文字数が分からないから最後から1文字目で指定するしかない
        middle_chars = list(word[1:-1])
        random.shuffle(middle_chars)
        return first_char + ''.join(middle_chars) + last_char

def shuffle_sentence(sentence):
    words = sentence.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)#「.join(リスト)」とすることで、リストを文字列として結合
    #.joinの前は空白を指定することで単語の間に空白を入れて文として結合させている

original_sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

shuffled_sentence = shuffle_sentence(original_sentence)
print("元の文:", original_sentence)
print("並び替えられた文:", shuffled_sentence)