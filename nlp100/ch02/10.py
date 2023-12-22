import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t', header=None)
line_count = len(df)
print(line_count)

