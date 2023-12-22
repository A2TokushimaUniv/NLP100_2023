import pandas as pd

def extract_columns(input_file, col1_output_file, col2_output_file):
    # テキストファイルをデータフレームとして読み込む
    df = pd.read_csv(input_file, sep='\t', header=None)

    # 1列目を抜き出し、col1.txtに保存する
    df[0].to_csv(col1_output_file, header=False, index=False)

    # 2列目を抜き出し、col2.txtに保存する
    df[1].to_csv(col2_output_file, header=False, index=False)

# 入力となるテキストファイルと出力先のファイルを指定
input_file_path = 'popular-names.txt'
col1_output_file_path = 'col1.txt'
col2_output_file_path = 'col2.txt'

# ファイルから1列目と2列目を抜き出して保存する
extract_columns(input_file_path, col1_output_file_path, col2_output_file_path)