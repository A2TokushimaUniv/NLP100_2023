import pandas as pd

def unique_values_in_column(file_path, column_index):
    # ファイルをデータフレームとして読み込む
    df = pd.read_csv(file_path, sep='\t', header=None, engine='python')

    # 指定した列のユニークな値を取得
    unique_values = df[column_index].unique()

    return unique_values

if __name__ == "__main__":
    file_path = 'popular-names.txt'  # ファイルのパスを指定
    column_index = 0  # 1列目の場合は0を指定

    unique_values = unique_values_in_column(file_path, column_index)

    print("Unique values in the first column:")
    for value in unique_values:
        print(value)

#python 17.py