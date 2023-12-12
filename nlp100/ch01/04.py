def create_word_position_map(sentence):
    words = sentence.split()
    word_position_map = {}

    for i, word in enumerate(words, 1):
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            # 先頭の1文字を取り出す
            extracted_chars = word[0]
        else:
            # 先頭の2文字を取り出す
            extracted_chars = word[:2]

        word_position_map[extracted_chars] = i

    return word_position_map

#　テキスト
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 連結
result_map = create_word_position_map(sentence)

# 結果の表示
print(result_map)