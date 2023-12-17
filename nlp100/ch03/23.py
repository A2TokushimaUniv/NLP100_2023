import pandas as pd
import re

def extract_sections(text): #文字列の抽出
   
    sections = re.findall(r'(==+)(.*?)\1', text) #文字列を見つけリストに変換
    return sections

def main():
  
    df = pd.read_json('jawiki-country.json.gz', lines=True) #ファイルを読み込みデータフレームに

    UK_article = df[df['title'] == 'イギリス'].iloc[0] #イギリスに関する記事の抽出

    sections = extract_sections(UK_article['text']) #リストの作成

    for level, section_name in sections: #各行に対する処理
        print(f"レベル {len(level) - 1}: {section_name}") #表示(レベル数の調整のための-1)

if __name__ == "__main__":
    main() #メイン関数の実行
