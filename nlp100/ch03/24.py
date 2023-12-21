import pandas as pd
import re

pattern = re.compile('File|ファイル:(.+?)\|')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    f = re.findall(pattern, line)
    if f:
        print (f[0])