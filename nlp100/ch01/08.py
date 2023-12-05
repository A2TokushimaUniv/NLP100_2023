#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(w):
    s = ""
    for i in w:
        if i.islower():
            s += chr(219 - ord(i))
        else:
            s += i
    return s

text = "Hello World"

print(f"暗号化:{cipher(text)}") 
print(f"復号化:{cipher(cipher(text))}") 
