import random
text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind '
text = text.replace('.','')
str = text.split(' ')
str1 = ""

for i in str:
    if len(i) <= 4:
        pass
    else:
        i = i[0]+''.join(random.sample(i[1:-1], len(i[1:-1])))+i[-1]
    str1 += i + ' '

text2 = str1[:-1] + '.'
print(text2)