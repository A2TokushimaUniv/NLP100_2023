# 03. 円周率Permalink
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# , と.を空白に置換　→　空白で文を分割
text_sub = text.replace(',', '').replace('.', '').split() 
# # []でリスト化する↓
Answer = [len(i) for i in text_sub]
print(Answer)
