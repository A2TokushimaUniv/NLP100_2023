str1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str2 = str1.replace(',','')
str3 = str2.replace('.','')
str4 = str3.split()

for i in range(0,15):
    str = len(str4[i])
    str4[i] = str
print(str4)