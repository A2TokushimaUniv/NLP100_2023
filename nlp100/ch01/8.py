def cipher(sentence):
    result = ""
    for char in sentence:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result


sentence = "Hello, THIS IS messaGE"
# 暗号化
encrypt_result = cipher(sentence)
print(encrypt_result)

# 復号化
decrypt_result = cipher(encrypt_result)
print(decrypt_result)
