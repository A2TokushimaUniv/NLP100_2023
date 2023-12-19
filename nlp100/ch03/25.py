# 25. テンプレートの抽出Permalink
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import re
import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in UK_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]
print(ans)