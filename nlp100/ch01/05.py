def ngram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
s = 'I am an NLPer'
print (ngram(s.split(),2))
print (ngram(s,2))