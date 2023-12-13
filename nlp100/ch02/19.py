#各行の1列目の文字列の出現頻度を求め，
# その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
answer = df[0].value_counts()#1列目の文字列の出現回数をカウント
answer = pd.DataFrame(answer)
answer = answer.reset_index()#番号を振りなおす
answer.columns = ['name','count']
answer = answer.sort_values(['count','name'],ascending=[False,False])
print (answer)