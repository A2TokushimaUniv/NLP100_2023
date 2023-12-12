# 15. 末尾のN行を出力Permalink
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

import pandas as pd
import sys

if len(sys.argv) == 1:
    print("引数も指定してください（例：python abc.py 5）")
else:
    N = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(df.tail(N))
