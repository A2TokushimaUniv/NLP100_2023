import re
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
