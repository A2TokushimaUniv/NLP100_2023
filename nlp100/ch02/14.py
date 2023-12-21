import pandas as pd
from sys import argv

if len(argv) == 1:
    print("Set arg 'n', 引数を入力してください！")
else:
    n = int(argv[1])
    df = pd.read_csv('./popular-names.txt',sep='\t', header=None)
    print(df.head(n))
