import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
df.to_csv('popular-names.txt', sep=' ',header=None, index=False)