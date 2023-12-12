sentence1 = "パトカー"
sentence2 = "タクシー"

sentence_length = min(len(sentence1), len(sentence2))

result = ""
for i in range(sentence_length):
    result += sentence1[i] + sentence2[i]
print(result)
