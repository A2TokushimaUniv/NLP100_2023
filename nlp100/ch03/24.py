# 24. ファイル参照の抽出Permalink
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
#正規表現 r'\[\[ファイル:([^\]|]+)' を使用して、↓
# [[ファイル: で始まり | もしくは ]] が現れるまでの文字列を抽出
for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', UK_text):
    print(file[1])