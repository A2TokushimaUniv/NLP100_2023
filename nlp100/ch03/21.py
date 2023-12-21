import re
pattern = "\[\[Category:.*?\]\]"
result = re.findall(pattern, UKtext)
result