import random

t = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
w = t.split()
for i,word in enumerate(w):
    if len(word) <= 4:
        continue
    start = word[0]
    end = word[-1]
    mid = list(word[1:-1])
    random.shuffle(mid)
    w[i] = start+"".join(mid)+end
print("変更前： ", t)
print("変更後： ", " ".join(w))