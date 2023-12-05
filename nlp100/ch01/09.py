import random

def shuffle_words(sentence):
   
    words = sentence.split()
    shuffled_words = []

    for word in words:
        if len(word) > 4:
            # 4ijou
            middle_chars = list(word[1:-1]) #startwords lastwords ha sonomama  soreigaiha middle ni kakunou
            random.shuffle(middle_chars)
            shuffled_word = word[0] + ''.join(middle_chars) + word[-1] #gattai
            shuffled_words.append(shuffled_word)
        else:
            # 4ika
            shuffled_words.append(word)

    return ' '.join(shuffled_words)

input_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

output_sentence = shuffle_words(input_sentence)

print("motonobun:", input_sentence)
print("narabikaegonobun:", output_sentence)