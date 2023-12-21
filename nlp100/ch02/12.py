basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f, open("{}col1.txt".format(basepath), "w") as fc1, open("{}col2.txt".format(basepath), "w") as fc2:
    lines = f.readlines()
    count = len(lines)
    for i, line in enumerate(lines):
      name, sex, _, _ = line.split(' ')
      if count == i:
        fc1.write(name)
        fc2.write(sex)
      else:
        fc1.write(name + '\n')
        fc2.write(sex + '\n')