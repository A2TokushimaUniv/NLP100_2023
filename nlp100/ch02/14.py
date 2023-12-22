#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
print (df.head(10))#引数で先頭からの行数を指定