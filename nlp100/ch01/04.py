w = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w = w.replace('.','')
n = [1, 5, 6, 7, 8, 9, 15, 16, 19]
a = {}
for m, s in enumerate(w.split()):
    if (m+1) in n:
        v = s[:1]
    else:
        v = s[:2]
    a[v] = m+1
print (a)