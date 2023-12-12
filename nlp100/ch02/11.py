# 11. タブをスペースに置換Permalink
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import pandas as pd


#引数headerを"None"とすると0始まりの連番が列名columnsになる
#デフォルトでは一行目がheaderとして認識され、列名columnsに割り当てられる。
pd2 = pd.read_csv('popular-names.txt', sep='\t', header=None)

#indexは（見出し列（行番号））
# 出力の有無は、引数header, indexにTrueかFalseで指定する。
pd2.to_csv('Ans_11.txt', sep = ' ', header=False, index=False)
#to_csv：書き込み