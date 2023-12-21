import pandas as pd
date = pd.read_csv('popular-names.txt',sep = '\t',header = None)
date['count'] = date.groupby(0)[0].transform('count')
print(date.sort_values(['count',0],reverse = True))