import re
inf_dic2 = {}
for key, text in inf_dic.items():
  inf_dic2[key] = re.sub(r'(\\\'){2,5}' , '', text)
inf_dic2