str1 = 'パトカー'
str2 = 'タクシー'
str3 = ''
for i in range(0,4):
    str = (str1 + str2)[i::4]
    str3 += str
print(str3)