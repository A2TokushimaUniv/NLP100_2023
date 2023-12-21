import pandas as pd
js = pd.read_json('jawiki-country.json.gz', lines = True)
uk = js[js['title'] == 'イギリス'].text.values
print(uk)