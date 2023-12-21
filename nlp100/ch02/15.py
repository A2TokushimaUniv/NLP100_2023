basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
    val = int(input())
    lines = f.readlines()
    count = len(lines) - 1
    for i in reversed(range(val)):
        result = lines[count - i].replace('\n', '')
        print(result)