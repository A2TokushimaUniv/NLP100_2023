import glob
file_list = glob.glob("col*.txt")
with open('col1.txt','r')as col1:
    lines = col1.readlines()
    num = len(lines)

with open('result.txt','w')as result:
    for i in range(0,num):
        for file_name in file_list:
            with open(file_name,'r')as infile:
                result.write(infile[i].read())
