# 27. 内部リンクの除去Permalink
# 26の処理に加えて，
# テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．

# 内部リンクを除去する関数「remove_inner_links()」を定義し適用
import re
import pandas as pd

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}


def remove_inner_links(dc):
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub(r'\2', v) for k, v in dc.items()}


df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in UK_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]
print(remove_inner_links(remove_stress(ans)))