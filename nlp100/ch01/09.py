import random

def shuffle_word(word):
    if len(word) <= 4:
        return word
    else:
        first_char = word[0]
        last_char = word[-1]
        middle_chars = list(word[1:-1])
        random.shuffle(middle_chars)
        return first_char + ''.join(middle_chars) + last_char

def shuffle_sentence(sentence):
    words = sentence.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)

original_sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

shuffled_sentence = shuffle_sentence(original_sentence)
print("元の文:", original_sentence)
print("並び替えられた文:", shuffled_sentence)