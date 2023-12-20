import re
pattern = '\[\[ファイル:(.*?)(?:\||\])'
result = re.findall(pattern, UKtext)
result