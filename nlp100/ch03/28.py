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
inf_dic4