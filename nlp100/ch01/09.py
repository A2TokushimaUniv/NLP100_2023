import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
l=[]
for i in s.split():
    if len(i) > 4:
        i = i[0] + "".join(random.sample(i[1:-1], len(i) - 2)) + i[-1]
    l.append(i)
print(" ".join(l))