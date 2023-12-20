with open('popular-names.txt')as text:
    date = text.read()
    print(date.replace('\t',' '))