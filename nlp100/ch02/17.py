#1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
s = df[0].unique()#1列目にユニーク関数を用いて文字列の重複をなくす
s.sort()#並び変える
print (s)