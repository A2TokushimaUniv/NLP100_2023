# 17. １列目の文字列の異なりPermalink
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

# pandasでデータを読み込み「unique()」で、異なる文字列の集合を取得
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df[0].unique())