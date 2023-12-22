#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

N = 3 #分割数を指定
import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
step = - (-len(df) // N)#分割する行数を計算
for n in range(N):
    df_split = df.iloc[n*step:(n+1)*step]
    df_split.to_csv('16_'+str(n)+'.txt', sep='\t',header=False, index=False)
