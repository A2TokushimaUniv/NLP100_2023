#記事から参照されているメディアファイルをすべて抜き出せ．

import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values
ls = uk[0].split('\n')

media = re.compile('File|ファイル:(.+?)\|')

for line in ls:
    r = re.findall(media, line)
    if r:
        print (r[0])
