basepath = "./"
with open("{}col1.txt".format(basepath), "r") as fc1, open("{}col2.txt".format(basepath), "r") as fc2, open("{}col1col2.txt".format(basepath), "w") as f:
    i = 0
    linesfc1 = fc1.readlines()
    linesfc2 = fc2.readlines()
    count = len(linesep)
    for name, sex in zip(linesfc1, linesfc2):
        name = name.replace("\n", "")
        sex = sex.replace("\n", "")
        i += 1
        if count == i:
            f.write(name + "\t" + sex)
        else:
            f.write(name + "\t" + sex + "\n")