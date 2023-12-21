import pandas as pd
import re

pattern = re.compile('\|(.+?)\s=\s*(.+)')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
dic = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        dic[r[1]]=r[2]
print (dic)