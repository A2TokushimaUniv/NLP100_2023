def cipher(s):
    angou =[]
    for i in s:
        if 97 <= ord(i) <= 122:
            i = chr(219-ord(i))
        angou.append(i)
    return ''.join(angou)
s = "I have a pen"
angou = cipher(s)
print (angou)
print (cipher(angou))