import requests
import pandas as pd
import re

def remove_markup(text): # 強調マークアップの除去
   
    text = re.sub(r"'''''(.*?)'''''", r"\1", text)  # 強い強調の除去
    text = re.sub(r"'''(.*?)'''", r"\1", text)      # 強調の除去
    text = re.sub(r"''(.*?)''", r"\1", text)        # 弱い強調の除去
    
    text = re.sub(r'\[\[([^|\]]*?\|)*(.*?)\]\]', r'\2', text) # 内部リンクマークアップを除去
    
    text = re.sub(r'\[([^|\]]*?\|)*(.*?)\]', r'\2', text) # 外部リンクマークアップを除去
    
    text = re.sub(r'\{\{([^|\}]*?\|)*(.*?)\}\}', r'\2', text) # テンプレートマークアップを除去
    
    return text

def get_flag_image_url(country_name):
    
    api_endpoint = 'https://ja.wikipedia.org/w/api.php' # Wikipedia API
    
    params = {  # ページの情報を取得
        'action': 'query',
        'format': 'json',
        'titles': country_name,
        'prop': 'revisions',
        'rvprop': 'content'
    }
    
    response = requests.get(api_endpoint, params=params)
    data = response.json()
    
    page = next(iter(data['query']['pages'].values())) # 基礎情報を取得
    content = page['revisions'][0]['*']
    
    flag_match = re.search(r'\|国旗画像\s*=\s*(.*?)\s*\|', content) # 国旗画像のファイル名no取得
    if flag_match:
        flag_filename = flag_match.group(1)
    else:
        return None

    params = {     # ファイル情報を取得
        'action': 'query',
        'format': 'json',
        'titles': f'File:{flag_filename}',
        'prop': 'imageinfo',
        'iiprop': 'url'
    }
    
    response = requests.get(api_endpoint, params=params)
    data = response.json()
    
    image_info = next(iter(data['query']['pages'].values()))      # 画像のURLを取得
    if 'imageinfo' in image_info:
        image_url = image_info['imageinfo'][0]['url']
        return image_url
    else:
        return None

def main():
    df = pd.read_json('jawiki-country.json.gz', lines=True) #
    UK_article = df[df['title'] == 'イギリス'].iloc[0] #
    
    flag_image_url = get_flag_image_url(remove_markup(UK_article['text'])) # テンプレートの基礎情報から国旗画像のURLを取得
    
    if flag_image_url:
        print(f"国旗画像のURL: {flag_image_url}") #
    else:
        print("国旗画像が見つかりませんでした。") #

if __name__ == "__main__":
    main()  #メイン関数の実行