basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
    lines = f.readlines()
    name = sorted(set(map(lambda x: x.split(' ')[0], lines)))
print(name)