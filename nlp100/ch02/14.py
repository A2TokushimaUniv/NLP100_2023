# 14. 先頭からN行を出力Permalink
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

#「python （ファイル名） hoge」として与えたコマンドライン引数は
# 「sys.argv」にリストとして格納されている

#リストの0番目の要素がファイル名、
# 1番目の要素が一つ目のコマンドライン引数，例：(python abc.py 5)

import pandas as pd
import sys

if len(sys.argv) == 1:
    print("引数も指定してください（例：python abc.py 5）")
else:
    N = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(df.head(N))
