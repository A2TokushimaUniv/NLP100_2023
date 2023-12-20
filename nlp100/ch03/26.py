#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values
ls = uk[0].split('\n')

template = re.compile('\|(.+?)\s=\s*(.+)')
d = {}

markup = re.compile('\'{2,}(.+?)\'{2,}')

for line in ls:
    r = re.search(template, line)
    if r:
        d[r[1]]=r[2]
        r = re.sub(markup,'\\1', line)
        print(r)
