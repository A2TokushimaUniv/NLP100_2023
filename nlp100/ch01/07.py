# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y=”気温”, z=22.4として，
# 実行結果を確認せよ．
def xyz_text(x,y,z):
    Answer = f"{x}時の{y}は{z}"
    return Answer

x = 12
y = "気温"
z = 22.4
text_Answer = xyz_text(x,y,z)
print(text_Answer)



