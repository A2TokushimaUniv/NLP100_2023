import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True) #ファイルを読み込みデータフレームに

df_UK = df[df['title']=='イギリス'].text.values #イギリスに関する記事の抽出(12/17 numpy配列の取得)

file = re.compile('File|ファイル:(.+?)\|') #fileという文字列を検索するためお正規表現パターンをコンパイル

fi = df_UK[0].split('\n') #行ごとに分割してリストを生成

for line in fi: #各行に対する処理
    sections = re.findall(file, line)  #文字列を見つけリストに変換
    if sections:
        print (sections[0]) #表示

