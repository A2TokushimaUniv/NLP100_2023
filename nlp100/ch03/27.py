import pandas as pd
import re

def remove_markup(text): # 強調マークアップの除去
   
    text = re.sub(r"'''''(.*?)'''''", r"\1", text)  # 強い強調の除去
    text = re.sub(r"'''(.*?)'''", r"\1", text)      # 強調の除去
    text = re.sub(r"''(.*?)''", r"\1", text)        # 弱い強調の除去
    
    text = re.sub(r'\[\[([^|\]]*?\|)*(.*?)\]\]', r'\2', text)  # 内部リンクマークアップを除去
    
    return text

def extract_infobox(text): #基礎情報テンプレートのフィールド名の抽出
    pattern = r'\{\{基礎情報(.*?)\n\}\}'
    infobox_match = re.search(pattern, text, re.DOTALL)

    if infobox_match: #
        infobox_content = infobox_match.group(1)
        fields = re.findall(r'\|([^=]+)\s*=\s*(.*?)\s*(?=\n\||\n\}\}$)', infobox_content, re.DOTALL) #文字列を見つけリストに変換
        
        infobox_dict = {key: remove_markup(value) for key, value in fields} # 強調マークアップと内部リンクマークアップを除去して格納
        return infobox_dict
    else:
        return None

def main():
    df = pd.read_json('jawiki-country.json.gz', lines=True) #ファイルを読み込みデータフレームに
    UK_article = df[df['title'] == 'イギリス'].iloc[0] #イギリスに関する記事の抽出(12/17 numpy配列の取得)
    infobox_data = extract_infobox(UK_article['text']) #格納

    if infobox_data:
        for key, value in infobox_data.items(): #
            print(f"{key}: {value}")
    else:
        print("基礎情報テンプレートが見つかりませんでした。") #

if __name__ == "__main__":
    main()