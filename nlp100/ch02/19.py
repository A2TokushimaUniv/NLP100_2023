from collections import Counter

with open("./popular-names.txt","r") as f:
    col1 = [line.split("\t")[0] for line in f.readlines()]

col1_dict = Counter(col1).most_common()
for d in col1_dict:
    print(d[0],d[1])