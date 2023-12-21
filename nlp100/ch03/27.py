import re
import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]

template_text = re.findall("\{\{基礎情報 (.+?^\}\})",text,re.MULTILINE+re.DOTALL)[0]

template_text = re.sub("'{2,5}" , "",template_text)
template_text = re.sub("\[\[(?:[^|]+?\|)??(([^|]+?)|(\{\{.?\}\}))\]\]",r"\1",template_text)

template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})",template_text,re.MULTILINE+re.DOTALL))

for key,value in template.items():
    print(key,value)