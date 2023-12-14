# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存Permalink
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import pandas as pd

pd2 = pd.read_csv('popular-names.txt', sep='\t', header=None)

#indexは（見出し列（行番号））
#上で列名を0~の数字に指定したので（header = None）, 列を下で指定できる
pd2[0].to_csv('col1.txt', index=False, header=False)
pd2[1].to_csv('col2.txt', index=False, header=False)