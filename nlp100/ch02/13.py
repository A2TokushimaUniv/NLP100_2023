import pandas as pd
df1 = pd.read_csv('col1.txt', delimiter='\t', header=None)
df2 = pd.read_csv('col2.txt', delimiter='\t', header=None)
df = pd.concat([df1, df2], axis=1)
df.to_csv('col1_2.txt', sep='\t',header=False, index=False)
