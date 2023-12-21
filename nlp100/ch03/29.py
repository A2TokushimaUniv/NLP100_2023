import pandas as pd
import re
import requests

pattern = re.compile('\|(.+?)\s=\s*(.+)')
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title']=='イギリス'].text.values
ls = uk[0].split('\n')
dic = {}
for line in ls:
    r = re.search(pattern, line)
    if r:
        dic[r[1]]=r[2]
        
S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + dic['国旗画像'],
    "prop": "imageinfo",
    "iiprop":"url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for k, v in PAGES.items():
    print (v['imageinfo'][0]['url'])