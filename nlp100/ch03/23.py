from df import UK_text as uk
import re

for section in re.findall(r'(=+)([^=]+)\1\n', uk):
    print(f'{section[1].strip()}\t{len(section[0]) - 1}')
