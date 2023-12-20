#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values

category = re.compile('Category')
ls = uk[0].split('\n')#行ごとに分割
for line in ls:
    if re.search(category, line):#カテゴリ名が宣言されていれば出力
        line = line.replace('[[','').replace('Category:','').replace(']]','').replace('|*','').replace('|元','')#名前以外を置換
        print (line)

