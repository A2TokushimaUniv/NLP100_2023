import pandas as pd

def sort_by_column(file_path, sort_column_index):
    # ファイルをデータフレームとして読み込む
    df = pd.read_csv(file_path, sep='\t', header=None, engine='python')

    # 3列目の数値の逆順でデータフレームをソートする
    sorted_df = df.sort_values(by=sort_column_index, ascending=False)

    return sorted_df

if __name__ == "__main__":
    file_path = 'popular-names.txt'  # ファイルのパスを指定
    sort_column_index = 2  # 3列目の場合は2を指定

    sorted_df = sort_by_column(file_path, sort_column_index)

    print("Sorted data by the third column in descending order:")
    print(sorted_df)

    # ソートしたデータフレームを新しいテキストファイルに保存する
    sorted_df.to_csv('sorted_output.txt', sep='\t', header=False, index=False)

    ##python 17.py