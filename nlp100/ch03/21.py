# 21. カテゴリ名を含む行を抽出Permalink
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)

#（例：‘ 列名 == “文字列“ ‘）
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n') #改行で分割

#記事中でカテゴリ名を宣言している行は「Category:」を含むので
#「filter」を用いて「Category:」を含む行のみを取り出す
Ans = list(filter(lambda x: '[Category:' in x, UK_texts))
print(Ans)