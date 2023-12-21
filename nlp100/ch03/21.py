import pandas as pd
from df import UK_text

UK_textn = UK_text.split('\n')
a = list(filter(lambda x: '[Category' in x, UK_textn))
print(a)
