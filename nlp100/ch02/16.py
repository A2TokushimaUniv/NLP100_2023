import numpy as np
basepath = "./"
with open("{}popular-names.txt".format(basepath), "r") as f:
    val = int(input())
    lines = f.readlines()
    count = len(lines)
    num_list = range(count)
    div_list = np.array_split(num_list, val)
    for i, div in enumerate(div_list, 1):
        f = open('{}{}.txt'.format(basepath, str(i).zfill(3)), 'w')
        for j in div:
            f.write(lines[j])
        f.close()