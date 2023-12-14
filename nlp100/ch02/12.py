import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
df.iloc[:,1].to_csv('col1.txt', sep=' ',header=False, index =False)
df.iloc[:,2].to_csv('col2.txt', sep=' ',header=False, index =False)