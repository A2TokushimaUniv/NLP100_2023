with open('popular-names.txt')as text, open('col1.txt','w')as text1, open('col2.txt','w')as text2:
    date = text.read()
    date = date.replace('\t',' ').replace('\n',' ')
    date = date.split()
    for i in date[::4]:
        text1.write(i)
        text1.write('\n')

    for i in date[1::4]:
        text2.write(i)
        text2.write('\n')
