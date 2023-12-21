import sys

args = sys.argv

with open('popular-names.txt')as text:
    date = text.readlines()
    for i in range(args[1]):
        date[i] = date[i].replace('\n','')
        print(date[i])
