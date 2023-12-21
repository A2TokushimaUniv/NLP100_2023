import re
import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]

template_text = re.findall("\{\{基礎情報 (.+?^\}\})",text,re.MULTILINE+re.DOTALL)[0]
template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})",template_text,re.MULTILINE+re.DOTALL))

for t in template:
    print(t,template[t])