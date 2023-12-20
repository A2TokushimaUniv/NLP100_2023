from df import UK_text as uk
import re

for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', uk):
    print(file[1])
