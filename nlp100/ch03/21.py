import pandas as pd
import re

df = pd.read_json('jawiki-country.json.gz', lines = True) #ファイルを読み込みデータフレームに

df_UK = df[df['title']=='イギリス'].text.values #イギリスに関する記事の抽出(12/17 numpy配列の取得)

category = re.compile('Category') #Categoryという文字列を検索するためお正規表現パターンをコンパイル

ca = df_UK[0].split('\n') #行ごとに分割してリストを生成

for line in ca: #各行に対する処理（Categoryが含まれている行の表示）
    if re.search(category, line): #Categoryが含まれていない行はNoneを返す
        print (line) #表示

