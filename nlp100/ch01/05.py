str1 = 'I am an NLPer'
char1 = []
word1 = []

def ngram(word,num):
    char = str1.replace(" ", "")
    word = str1.split(" ")
    for i in range(len(char)):
        char1.append(char[i:num+i])
    for j in range(len(word)):
        word1.append(word[j:num+j])

ngram(str1, 2)

print('単語bi-gram',word1)
print('文字bi-gram',char1)