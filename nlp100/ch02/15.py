#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
print (df.tail(10))#引数で末尾からの行数を指定
