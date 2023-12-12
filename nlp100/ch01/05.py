def get_ngram(s,n):
  n_gram =[]
  executions = len(s)-n+1
  start = 0
  end = n
  for _ in range(executions):
    n_gram.append(s[start:end])
    start +=1
    end +=1
  return n_gram

sentence = input("Input sentence : ")
sentence = sentence.split(" ")
n_gram = get_ngram(sentence,2)
print(n_gram)
