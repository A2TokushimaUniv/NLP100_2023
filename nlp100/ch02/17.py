with open("./popular-names.txt","r") as f:
    col1 = [line.split("\t")[0] for line in f.readlines()]   
    col1 = sorted(set(col1))
for c in col1:
    print(c)