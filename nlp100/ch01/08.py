lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inp = input()
n = ''
for i in inp:
  if i in lowercase:
    n += chr(219 - ord(i))
    continue
  n += i
print(n)