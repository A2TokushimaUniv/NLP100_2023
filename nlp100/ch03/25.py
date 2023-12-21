import pandas as pd
import re

def extract_infobox(text): #基礎情報テンプレートのフィールド名の抽出
    
    pattern = r'\{\{基礎情報(.*?)\n\}\}'
    infobox_match = re.search(pattern, text, re.DOTALL)

    if infobox_match:
        infobox_content = infobox_match.group(1)
        
        fields = re.findall(r'\|([^=]+)\s*=\s*(.*?)\s*(?=\n\||\n\}\}$)', infobox_content, re.DOTALL) #文字列を見つけリストに変換
        infobox_dict = dict(fields)
        return infobox_dict
    else:
        return None

def main(): #メイン関数
    df = pd.read_json('jawiki-country.json.gz', lines=True) #ファイルを読み込みデータフレームに
    UK_article = df[df['title'] == 'イギリス'].iloc[0] #イギリスに関する記事の抽出(12/17 numpy配列の取得)
    infobox_data = extract_infobox(UK_article['text']) #格納

    if infobox_data:
        
        for key, value in infobox_data.items():
            print(f"{key}: {value}")
    else:
        print("基礎情報テンプレートが見つかりませんでした。")

if __name__ == "__main__":
   
    main()



 ##後で確認