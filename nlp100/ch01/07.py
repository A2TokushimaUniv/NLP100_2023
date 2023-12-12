# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y=”気温”, z=22.4として，
# 実行結果を確認せよ．

def generate_sentence(x, y, z):
    result = f"{x}時の{y}は{z}"
    return result

x_value = 12
y_label = "気温"
z_value = 22.4

result_sentence = generate_sentence(x_value, y_label, z_value)
print(result_sentence)