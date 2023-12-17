import pandas as pd
import re

def extract_categories(text): #カテゴリ名の抽出をする関数
    
    categories = re.findall(r'\[\[Category:(.*?)\]\]', text) #文字列を見つけリストに変換

    return categories

df = pd.read_json('jawiki-country.json.gz', lines=True) #ファイルを読み込みデータフレームに

UK_article = df[df['title'] == 'イギリス'].iloc[0] #イギリスに関する記事の抽出

categories = extract_categories(UK_article['text']) #関数の使用

for category in categories:
    print(category)   # 表示