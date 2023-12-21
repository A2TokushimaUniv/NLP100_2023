import pandas as pd
import re

pattern = re.compile('\|(.+?)\s=\s*(.+)')
kyoutyou = re.compile('\'{2,}(.+?)\'{2,}')
link= re.compile('\[\[(.+?)\]\]')
mw = re.compile('<[br|ref][^>]*?>.+?<\/[br|ref][^>]*?>')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title']=='イギリス'].text.values
lines = uk[0]
lines = re.sub(kyoutyou,'\\1', lines)
lines = re.sub(link,'\\1', lines)
lines = re.sub(mw,'', lines)
ls = lines.split('\n')
dict = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        dict[r[1]]=r[2]
print (dict)