#テンプレートの内容を利用し，
# 国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，
# ファイル参照をURLに変換すればよい）

import pandas as pd
import re
import requests
template = re.compile('\|(.+?)\s=\s*(.+)')
df = pd.read_json('jawiki-country.json.gz', lines = True)
uk = df[df['title']=='イギリス'].text.values
ls = uk[0].split('\n')
d = {}
for line in ls:
    r = re.search(template, line)
    if r:
        d[r[1]]=r[2]
        
S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + d['国旗画像'],
    "prop": "imageinfo",
    "iiprop":"url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for k, v in PAGES.items():
    print (v['imageinfo'][0]['url'])
