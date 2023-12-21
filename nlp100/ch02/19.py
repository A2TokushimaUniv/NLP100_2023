import collections
basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
  lines = f.readlines()
  temp = list(map(lambda x: x.split(' '), lines))
  c = collections.Counter(map(lambda x: x[0], temp))
  c2 = c.most_common()
print(c2)