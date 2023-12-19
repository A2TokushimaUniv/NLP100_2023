# 10. 行数のカウントPermalink
# 行数をカウントせよ．確認にはwcコマンドを用いよ

import pandas as pd

#引数headerを"None"とすると0始まりの連番が列名columnsになる
# タブで区切っている（\t）
line_count = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(len(line_count))