text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w = text.split(" ")
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = []
for i,w in enumerate(w):
  if i+1 in one:ans.append(w[0])
  else:ans.append(w[:2])
print(ans)