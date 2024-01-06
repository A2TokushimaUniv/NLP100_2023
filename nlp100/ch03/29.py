import urllib
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
  inf_dic4 = {}
for key, text in inf_dic3.items():
  pattern = '\{\{.*?\{\{center\|' 
  text = re.sub(pattern, '', text)

  pattern = '\{\{.*?\|.*?\|.{2}\|'
  text = re.sub(pattern, '', text) 

  pattern = '\<ref.*?\>.*?\<\/ref\>'
  text = re.sub(pattern, '', text)

  pattern = '\<ref.*?\>|\<br \/\>'
  text = re.sub(pattern, '', text)

  pattern = '\{\{lang\|.*?\|'
  text = re.sub(pattern, '', text)

  pattern = '\{\{.*?\}\}'
  text = re.sub(pattern, '', text)

  pattern = '\}\}'
  text = re.sub(pattern, '', text)

  inf_dic4[key] = text
print(inf_dic4)
url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:' + urllib.parse.quote(inf_dic4['国旗画像']) + '&format=json&prop=imageinfo&iiprop=url'
connection = urllib.request.urlopen(urllib.request.Request(url))
response = json.loads(connection.read().decode())
print(response['query']['pages']['-1']['imageinfo'][0]['url'])