import pandas as pd

def count_and_sort_by_frequency(file_path):
    # ファイルをデータフレームとして読み込む
    df = pd.read_csv(file_path, sep='\t', header=None, engine='python')

    # 1列目の文字列の出現頻度を求める
    frequency_counts = df[0].value_counts()

    # 出現頻度の高い順に並べる
    sorted_frequency = frequency_counts.sort_values(ascending=False)

    return sorted_frequency

if __name__ == "__main__":
    file_path = 'popular-names.txt'  # ファイルのパスを指定

    sorted_frequency = count_and_sort_by_frequency(file_path)

    print("Frequency of values in the first column (high to low):")
    print(sorted_frequency)