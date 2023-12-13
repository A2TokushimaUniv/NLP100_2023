import re
str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str2 = re.findall('[a-z]+', str1, flags=re.IGNORECASE)

def wordTake(num, word):
    if num in [1,5,6,7,8,9,15,16,19]:
        return(word[0],num)
    else:
        return(word[:2],num)
str3 = [wordTake(num,word) for num , word in enumerate(str2,1)]
print(dict(str3))