#記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values

section = re.compile('^=+.*=+$')# 1回以上の=で始まり、1回以上の=で終わる文字列

ls = uk[0].split('\n')

for line in ls:
    if re.search(section, line):
        level = line.count('=') // 2 - 1 #レベルを求める
        print(line.replace('=',''), level)  