from df import List as li
import re

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}

def remove_links(dc):
    r = re.compile(r'\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub(r'\2', v) for k, v in dc.items()}

print(remove_links(remove_stress(li)))
