import pandas as pd
from sys import argv

if len(argv) == 1:
    print("Set arg 'n', 引数を入力してください！")
else:
    n = int(argv[1])
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    print(len(df) // n)
    nrow = len(df)//n
    
    for i in range(n):
        df.loc[nrow*i : nrow*(i+1)].to_csv(f'./ans16_{i}', sep='\t', index=False, header=None)