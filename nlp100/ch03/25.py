#記事中に含まれる「基礎情報」テンプレートの
# フィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values
ls = uk[0].split('\n')

template = re.compile('\|(.+?)\s=\s*(.+)')
d = {}

for line in ls:
    r = re.search(template, line)
    if r:
        d[r[1]]=r[2]
print (d)