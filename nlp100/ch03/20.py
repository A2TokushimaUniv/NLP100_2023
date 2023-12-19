# 20. JSONデータの読み込みPermalink
# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
#各要素の値valueに対してforループ処理を行うには、
# values()メソッドを使う。
print(UK_text)