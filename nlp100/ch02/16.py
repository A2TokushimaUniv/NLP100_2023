# 16. ファイルをN分割するPermalink
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import pandas as pd
import sys

if len(sys.argv) == 1:
    print("引数も指定してください（例：python abc.py 5）")
else:
    N = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    nrow = -(-len(df) // N)
    #aをbで割った商の整数値：//

    for i in range(N):#loc[]を用いて行数指定でデータを分割して保存しています。
        df.loc[nrow*i : nrow*(i+1)].to_csv(f'ans16_{i}', sep='\t', header=False, index=False)