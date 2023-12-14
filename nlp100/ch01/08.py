def cipher(input_text):
    
    result_text = "" #imikakunin
    for char in input_text:
        if char.islower():
           
            result_text += chr(219 - ord(char))

        else:
           
            result_text += char

    return result_text

message = "Hello, World!"

encrypted_message = cipher(message)
print("angoukamessage:", encrypted_message)

decrypted_message = cipher(encrypted_message)
print("fukugoukamessage:", decrypted_message)