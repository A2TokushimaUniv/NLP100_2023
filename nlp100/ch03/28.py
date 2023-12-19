# 28. MediaWikiマークアップの除去Permalink
# 27の処理に加えて，
# テンプレートの値からMediaWikiマークアップを可能な限り除去し，
# 国の基本情報を整形せよ

# MediaWikiマークアップを除去する関数「remove_mk()」を定義し適用
import re
import pandas as pd

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}


def remove_inner_links(dc):
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub(r'\2', v) for k, v in dc.items()}


def remove_mk(v):
    r1 = re.compile("'+")
    r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')
    v = r1.sub('', v)
    v = r2.sub(r'\2', v)
    v = r3.sub(r'\2', v)
    v = r4.sub('', v)
    return v


df = pd.read_json('jawiki-country.json.gz', lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
UK_texts = UK_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in UK_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]

r = re.compile('\[\[(.+\||)(.+?)\]\]')
ans = {k: r.sub(r'\2', remove_mk(v)) for k, v in ans.items()}
print(remove_inner_links(remove_stress(ans)))