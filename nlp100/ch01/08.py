# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# ↓↓↓
# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力

# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def chipher(text):
    Answer = ""
    #文字コードを得るには「ord()」
    #逆に文字コードから文字を得る場合は「chr()」
    #chr関数はUnicodeコードポイントから文字を生成する。
    for word in text:
        if word.islower(): #英小文字ならば
            Answer += chr(219 - ord(word))
        else:
            Answer += word
    return Answer

message = "This is 2-PM." 
#暗号化
key_text = chipher(message)
#複合化
not_key_text = chipher(key_text)
print(f"暗号化されたメッセージ:{key_text}")
print(f"復号化されたメッセージ:{not_key_text}")
