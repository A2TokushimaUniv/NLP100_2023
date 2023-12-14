# coding: UTF-8

string = "abcdefgh"

#odd_string = "".join([string[i] for i in range(len(string)) if i % 2 == 0])

odd_string = (string[0::2])

print(odd_string)