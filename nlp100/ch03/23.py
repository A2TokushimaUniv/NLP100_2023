import pandas as pd
import re

pattern = re.compile('^=+.*=+$')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        level = line.count('=') / 2 - 1
        print(line.replace('=',''), int(level))