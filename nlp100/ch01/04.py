# 04. 元素記号Permalink
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭の2文字を取り出し，取り出した文字列から
# 単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）
# を作成せよ

text1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text2 = text1.replace('.', '').split()

def word_pick(text):
    answer_map = {}  #辞書型変数を作成
    top1_mozi = [1, 5, 6, 7, 8, 9, 15, 16, 19] # ↓先頭の一文字をとりだす単語を指定
    for i, word in enumerate(text, 1):
        if i in top1_mozi:
            answer_map[i] = word[0] #1文字目を代入
        else:
            answer_map[i] = word[:2] #2,3文字目を代入
    return answer_map


Answer_map = word_pick(text2)
print(Answer_map)