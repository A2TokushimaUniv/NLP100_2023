def get_char_ngram(word,n):
    char_n_gram = []
    executions = len(word)-n+1
    start = 0
    end = n
    for _ in range(executions):
        char_n_gram.append(word[start:end])
        start +=1
        end +=1
    return set(char_n_gram)
n = 2
A = 'paraparaparadise'
B = 'paragraph'
A = get_char_ngram(A,n)
B = get_char_ngram(B,n)
print('和集合 : {}'.format(A | B))
print('積集合 : {}'.format(A & B))
print('差集合 : {}'.format(A - B))