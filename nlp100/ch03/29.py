import requests
import re
import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]

template_text = re.findall("\{\{基礎情報 (.+?^\}\})",text,re.MULTILINE+re.DOTALL)[0]

'''template_text = re.sub("'{2,5}" , "",template_text)
template_text = re.sub("\[\[(?:[^|]+?\|)??(([^|]+?)|(\{\{.?\}\}))\]\]",r"\1",template_text)

template_text = re.sub("\[\[ファイル:(.+?)(?:\|.+)*\]\]",r"\1",template_text)
template_text = re.sub("\{\{lang\|.+?\|(.+?)\}\}",r"\1",template_text)
template_text = re.sub("\{\{仮リンク\|(.+?)\|.+?\}\}",r"\1",template_text)
template_text = re.sub("\{\{.+?\}\}","",template_text)
template_text = re.sub("<.+?>","",template_text)
template_text = re.sub("\[.+?]","",template_text)'''

template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})",template_text,re.MULTILINE+re.DOTALL))

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"
path = template["国旗画像"].replace(" ","_")

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop":"url",
    "titles": "File:"+path
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])