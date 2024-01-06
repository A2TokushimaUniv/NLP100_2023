import re
import json
text_list = []
pattern = '\[\[Category:.*?\]\]'

with open('jawiki-country.json','r',encoding = "utf-8")as file:
    line = file.readlines()
    for i in line:
        text_list.append(json.loads(i))
for i in range(len(text_list)):
    if text_list[i]['title']=='イギリス':
        UK_text = str(text_list[i])
        break
result = re.findall(pattern,UK_text)
print(result)