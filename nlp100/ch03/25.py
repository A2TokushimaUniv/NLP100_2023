import re
pattern = '基礎情報(.*?\<references/\>)'
result = re.findall(pattern, UKtext)
result[0] += "\\n"
pattern = '(?<=\\\\n\|)(.*?) *= *(.*?)(?=\\\\n)'
result2 = re.findall(pattern, result[0])
inf_dic = {}
for i, j in result2:
  inf_dic[i] = j
inf_dic