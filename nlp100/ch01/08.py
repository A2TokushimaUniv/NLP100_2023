# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力

# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result

# メッセージの例
original_message = "Hello, World! 123"

# 暗号化
encrypted_message = cipher(original_message)
print("暗号化されたメッセージ:", encrypted_message)

# 復号化
decrypted_message = cipher(encrypted_message)
print("復号化されたメッセージ:", decrypted_message)