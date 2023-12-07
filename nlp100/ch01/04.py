s ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s =s.replace('.','')
itimozi = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
for i, genso in enumerate(s.split()):
    if i+1 in itimozi:
        dic[genso[:1]] = i+1
    else:
        dic[genso[:2]] = i+1
print (dic)