import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
df.sort_values(2, ascending=False)