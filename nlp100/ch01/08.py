def cipher (sentense):
    # 変数を用意
    sentenseList = []
    result = ''

    for i in range (0, len(sentense)):
        # i番目の文字が小文字の場合
        if sentense[i].islower():
            # リストのi番目にアスキーコード(219-アスキーコード)に対応する文字を挿入
            sentenseList.insert(i, chr(219-ord(sentense[i])))
        # i番目の文字が小文字ではない場合そのままリストに挿入
        else:
            sentenseList.insert(i, sentense[i])
                
    # リストを文字列に戻す
    for n in range (0, len(sentense)):
        result += sentenseList[n]
        
    #文字列を返す
    return result
        
s = 'I am an NLPer'
new = cipher(s)
print ('暗号化' + new)

print ('複合化' + cipher(new))