basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
    val = int(input())
    lines = f.readlines()
    for i in range(val):
        lines[i] = lines[i].replace('\n', '')
        print(lines[i])