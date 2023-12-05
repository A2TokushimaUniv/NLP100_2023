import random

def change_char_order(li):
  result = []
  for i in li:
    if len(i) >= 4:
      result.append(randam_order(i))
      continue
    result.append(i)
  return result

def randam_order(word):
  first = 1
  end = -1
  res = ''
  pre_inner_word = word[first:end]
  length = len(pre_inner_word)
  random_list=[random.random() for i in range(length)]
  comb_list = zip(random_list,pre_inner_word)
  comb_list = sorted(comb_list,key=lambda x:x[0])
  _,sorted_char = zip(*comb_list) 
  for i in sorted_char:
    res += i
  return str(word[0]) + res + str(word[-1])

s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
s = s.split(' ')
print(s)
r = change_char_order(s)
print(r)