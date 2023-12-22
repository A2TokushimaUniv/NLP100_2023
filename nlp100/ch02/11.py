import pandas as pd

def replace_tabs_with_spaces(input_file, output_file):
    # テキストファイルをデータフレームとして読み込む
    df = pd.read_csv(input_file, sep='\t', header=None)

    # データフレーム内の全ての要素に対して、タブをスペースに置換する
    df = df.applymap(lambda x: str(x).replace('\t', ' '))

    # 置換後のデータフレームを新しいテキストファイルに保存する
    df.to_csv(output_file, sep=' ', header=False, index=False)

# 入力となるテキストファイルと出力先のファイルを指定
input_file_path = 'popular-names.txt'
output_file_path = 'new-popular-names.txt'

# ファイルのタブをスペースに置換する
replace_tabs_with_spaces(input_file_path, output_file_path)