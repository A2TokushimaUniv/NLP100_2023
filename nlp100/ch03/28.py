from df import List
import re

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

r = re.compile(r'\[\[(.+\||)(.+?)\]\]')
List = {k: r.sub(r'\2', remove_mw(v)) for k, v, in List.items()}
print(remove_links(remove_stress(List)))
