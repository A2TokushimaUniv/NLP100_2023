import pandas as pd
import re

pattern = re.compile('\|(.+?)\s=\s*(.+)')
kyoutyou = re.compile('\'{2,}(.+?)\'{2,}')
link = re.compile('\[\[(.+?)\]\]')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title'] == 'イギリス'].text.values
lines = uk[0]
lines = re.sub(kyoutyou,'\\1', lines)
lines = re.sub(link,'\\1', lines)
ls = uk[0].split('\n')
dic = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        dic[r[1]]=r[2]
print (dic)