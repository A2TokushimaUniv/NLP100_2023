# 26. 強調マークアップの除去Permalink
# 25の処理時に，
# テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去して
# テキストに変換せよ（参考: マークアップ早見表）．


# 強調マークアップを除去する関数「remove_stress()」を定義し適用
import re
import pandas as pd

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}


df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in UK_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]
print(remove_stress(ans))