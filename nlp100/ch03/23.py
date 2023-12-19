# 23. セクション構造Permalink
# 記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ．

import re
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]

#正規表現 r'(==+)([^=]+)\1' を使用してセクション名を抽出している
#　== が1回以上続き、その後にセクション名が続き、↓
# 再び == が来るパターンを探している
for section in re.findall(r'(=+)([^=]+)\1\n', UK_text):
    print(f'{section[1].strip()}\t{len(section[0]) - 1}')
    #セクション名とレベルはそれぞれ section[1] と len(section[0]) - 1 で取得