with open('popular-names.txt')as text:
    date = text.read()
    date = date.replace('\t',' ').replace('\n',' ')
    list_date  = date.split(' ')
    num = len(date) / 5
    result = []
    for i in range(int(num)):
        result.append(list_date[i : 4 + i])
    result.sort(reverse = True)
    print(result)
    
