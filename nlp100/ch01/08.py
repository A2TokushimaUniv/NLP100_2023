import re

def cipher(text):
    comp = re.compile('[a-z]')
    str = ""
    for i in text:
        if re.match(comp, i):
            i = chr(219 - ord(i))
        str += i
    return str

encode = cipher("I am an NLPer")
decode = cipher(encode)

print("暗号化:",encode)
print("復号化:",decode)