import re
import json
text_list = []

with open('jawiki-country.json','r',encoding = "utf-8")as file:
    line = file.readlines()
    for i in line:
        text_list.append(json.loads(i))
for i in range(len(text_list)):
    if text_list[i]['title']=='イギリス':
        UK_text = str(text_list[i])
        break
pattern = '基礎情報(.*?\<references>/\>)'
result = re.findall(pattern,UK_text)
result[0] += "\\n"
pattern = '(?<=\\\\n\|)(.*?) *= *(/*?)(?=\\\\n)'
result2 = re.findall(pattern,result[0])
inf_dic = {}
for i,j in result2:
    inf_dic[i] = j
print(inf_dic)
inf_dic2 = {}
for key, text in inf_dic.items():
    inf_dic2[key] = re.sub(r'(\\\'){2,5}', '',text)
print(inf_dic2)
inf_dic3 = {}
for key, text in inf_dic2.items():
  pattern = "(?<=\}\}\<br \/\>（)\[{2}"
  text = re.sub(pattern, '', text)

  pattern = "\[{2}.*?\|.*?px\|(?=.*?\]\])"
  text = re.sub(pattern, '', text)

  pattern = "(?<=(\|))\[{2}"
  text = re.sub(pattern, '', text)

  pattern = "(?<=\}{2}（)\[{2}"
  text = re.sub(pattern, '', text)

  pattern = "(?<=\>（)\[{2}.*?\|"
  text = re.sub(pattern, '', text)

  pattern = "(?<=（.{4}).*?\[{2}.*?\)\|" 
  text = re.sub(pattern, '', text)

  pattern = "\[{2}.*?\|"
  text = re.sub(pattern, '', text)

  pattern = "(\[{2}|\]{2})"
  inf_dic3[key] = re.sub(pattern, '', text)
print(inf_dic3)