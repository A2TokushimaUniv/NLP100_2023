import re
import json
import collections
pattern = '(={2,4}.*?={2,4})'
text_list = []
section = {}
with open('jawiki-country.json','r',encoding = "utf-8")as file:
    line = file.readlines()
    for i in line:
        text_list.append(json.loads(i))
for i in range(len(text_list)):
    if text_list[i]['title']=='イギリス':
        UK_text = str(text_list[i])
        break
result = re.findall(pattern,UK_text)
for text in result:
    c1 = collections.Counter(text)
    c2 = int(c1['=']/2) - 1
    text = text.replace('=','')
    section[text] = c2
print(section)