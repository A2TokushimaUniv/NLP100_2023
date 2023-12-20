import collections
import re
pattern = "(={2,4}.*?={2,4})"
result = re.findall(pattern, UKtext)
section = {}
for text in result:
    c1 = collections.Counter(text)
    c2 = int(c1['=']/2) - 1
    text = text.replace('=', '')
    section[text] = c2
section