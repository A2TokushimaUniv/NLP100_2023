import re
import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]
section = re.findall("(={2,4})(.+?)={2,}",text)
section = [[sec[1],len(sec[0])-1] for sec in section]
for i in section:
    print(i)