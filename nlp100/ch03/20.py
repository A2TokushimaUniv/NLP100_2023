import pandas as pd

df = pd.read_json("./jawiki-country.json", lines=True)
UK_text = df.query('title=="イギリス"')['text'].values[0]
print(UK_text)