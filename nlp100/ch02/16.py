import sys

args = sys.argv

with open('popular-names.txt')as text:
    date = text.readlines()
    num = len(date)
    count = num / args[1]


    for j in range(count):
        for i in range(args[1]):
            date[i] = date[i].replace('\n','')
            print(date[i])
        print('\n')