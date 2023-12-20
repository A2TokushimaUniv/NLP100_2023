import re
import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]

media = re.findall("\[\[ファイル:(.+?)(?:\|.+)*\]\]",text)
for m in media:
    print(m)