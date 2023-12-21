from df import List
import re
import requests

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}

def remove_links(dc):
    r = re.compile(r'\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub(r'\2', v) for k, v in dc.items()}

def remove_mw(v):
    r1 = re.compile(r"'+")
    r2 = re.compile(r'\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile(r'\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile(r'<\s*?/*?\s*?br\s*?/*?\s*>')
    v = r1.sub('', v)
    v = r2.sub(r'\2', v)
    v = r3.sub(r'\2', v)
    v = r4.sub('', v)
    return v

def get_url(dc):
    url_file = dc['国旗画像'].replace(' ','_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"', data.text).group(1)

r = re.compile(r'\[\[(.+\||)(.+?)\]\]')
List = {k: r.sub(r'\2', remove_mw(v)) for k, v in List.items()}

print(get_url(remove_links(remove_stress(List))))
