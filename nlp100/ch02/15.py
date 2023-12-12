n = 10
with open("./popular-names.txt","r") as f:
    lines = f.readlines()[-n:]
    print("".join(lines))