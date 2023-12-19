# 22. カテゴリ名の抽出Permalink
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n')

#「21. カテゴリ名を含む行を抽出」で取り出した行から、
# 余計な部分を「replace()」で削除
Ans = list(filter(lambda x: '[Category:' in x, UK_texts))

Ans = [a.replace('[[Category:', '').replace('|*', '').replace(']]', '') for a in Ans]
print(Ans)