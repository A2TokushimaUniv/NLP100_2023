import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines = True) #ファイルを読み込みデータフレームに

df_UK = df[df['title']=='イギリス'].text.values #イギリスに関する記事の抽出(12/17 numpy配列の取得)

print (df_UK) #表示