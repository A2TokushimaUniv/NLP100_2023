import json
import re
text_list = []
basepath = "[PATH]"
with open('./jawiki-country.json'.format(basepath), 'r') as f:
    lines = f.readlines()
    for line in lines:
        text_list.append(json.loads(line))

for i in range(len(text_list)):
    if text_list[i]['title']=="イギリス":
        UKtext = str(text_list[i])
        break
UKtext