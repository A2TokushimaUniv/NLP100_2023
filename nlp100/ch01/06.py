def ngram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
s1 = 'paraparaparadise'
s2 = 'paragraph'
st1 = set(ngram(s1, 2))
st2 = set(ngram(s2, 2))
#和集合、積集合、差集合
print(st1 | st2)
print(st1 & st2)
print(st1 - st2)
if 'se' in st1:
    print('st1にseは含まれる')
else:
   print('st1にseは含まれない')
if 'se' in st2:
    print('st2にseは含まれる')
else:
   print('st2にseは含まれない')