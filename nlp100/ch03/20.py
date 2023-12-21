import json
with open("./jawiki-country.json","r") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]
            print(text)
            break
