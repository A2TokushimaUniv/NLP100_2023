#12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

import pandas as pd
df1 = pd.read_csv('col1.txt', delimiter='\t', header=None)
df2 = pd.read_csv('col2.txt', delimiter='\t', header=None)
df = pd.concat([df1, df2], axis=1) #結合
df.to_csv('13.txt', sep='\t',header=False, index=False)
