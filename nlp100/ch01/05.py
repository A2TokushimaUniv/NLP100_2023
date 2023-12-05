def generate_ngram(sequence, n):
    
    ngram_list = []
    for i in range(len(sequence) - n + 1):
        ngram = sequence[i:i + n]
        ngram_list.append(ngram)
    return ngram_list

text = "I am an NLPer"

word_tokens = text.split()

word_bigrams = generate_ngram(word_tokens, 2)  

char_bigrams = generate_ngram(text, 2)

print("tangobi-gram:", word_bigrams)
print("mojibi-gram:", char_bigrams)