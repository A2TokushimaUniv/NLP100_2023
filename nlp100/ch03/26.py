from df import List
import re

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}

print(remove_stress(List))