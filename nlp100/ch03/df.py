import pandas as pd
import re

df = pd.read_json("./jawiki-country.json", lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_textn = UK_text.split('\n')
ans = list(filter(lambda x: '[Category' in x, UK_textn))
List = {}
p = re.compile(r'\|(.+?)\s=\s*(.+)')
for line in UK_textn:
    r = re.search(p, line)
    if r:
        List[r[1]] = r[2]
        
