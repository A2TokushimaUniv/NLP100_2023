with open('popular-names.txt')as text:
    date = text.read()
    date = date.replace('\t',' ').replace('\n',' ')
    date = date.split()
    for i in date[::4]:
        text1 = i
        print(text1) 