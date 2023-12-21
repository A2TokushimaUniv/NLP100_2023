import sys

args = sys.argv

with open('popular-names.txt')as text:
    date = text.readlines()
    count = len(date) - 1
    for i in reversed(range(args[1])):
        file = date[count - i].replace('\n','')
        print(file)