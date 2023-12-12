# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列↓
# 「パタトクカシーー」を得よ．

text1 = "パトカー"
text2 = "タクシー"
Answer = ""
def mix_text(_text1, _text2):
    mix = ""
    for i in range(len(_text1)):
        mix += _text1[i]
        mix += _text2[i]
    return mix

Answer = mix_text(text1, text2)
print(Answer)