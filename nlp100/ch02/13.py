# 13. col1.txtとcol2.txtをマージPermalink

# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．
import pandas as pd

c1 = pd.read_csv('col1.txt', header=None)#indexは0始まりの連番となる
c2 = pd.read_csv('col2.txt', header=None)#区切りsepは1列しかないのでいらない

Answer = pd.concat([c1, c2], axis=1)
#axis = 0（縦方向に連結）※デフォルト
# axis = 1（横方向に連結）

Answer.to_csv('Ans_13.txt',sep='\t', header=False, index=False)