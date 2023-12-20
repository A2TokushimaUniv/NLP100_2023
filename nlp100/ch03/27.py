#26の処理に加えて，テンプレートの値から
# MediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values
ls = uk[0].split('\n')

template = re.compile('\|(.+?)\s=\s*(.+)')
d = {}

markup = re.compile('\'{2,}(.+?)\'{2,}')

link = re.compile('\[\[(.+?)\]\]')

lines = uk[0]
lines = re.sub(markup, '\\1', lines)
lines = re.sub(link,'\\1', lines)
ls = lines.split('\n')

for line in ls:
    r = re.search(template, line)
    if r:
        d[r[1]]=r[2]
print (d)

