#記事中でカテゴリ名を宣言している行を抽出せよ

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values

category = re.compile('Category')
ls = uk[0].split('\n')#行ごとに分割
for line in ls:
    if re.search(category, line):#カテゴリ名が宣言されていれば出力
        print(line)
