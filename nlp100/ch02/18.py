basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
  lines = f.readlines()
  lines = map(lambda x: x.replace("\n",""), lines)
  temp = list(map(lambda x: x.split(' '), lines))
  pnum = sorted(temp, key=lambda x: int(x[2]), reverse=True)
print(pnum)