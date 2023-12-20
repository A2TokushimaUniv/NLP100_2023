from df import UK_textn as uk
import re

p = re.compile(r'\|(.+?)\s=\s*(.+)')
a = {}
for line in uk:
    r = re.search(p, line)
    if r:
        a[r[1]] = r[2]
print(a)