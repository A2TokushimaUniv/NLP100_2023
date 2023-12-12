import sys
import pandas as pd

def split_file(file_path, n):
    # ファイルをデータフレームとして読み込む
    df = pd.read_csv(file_path, sep='\t', header=None, engine='python')

    # 行単位でN分割する
    split_data = [df.iloc[i:i + n] for i in range(0, len(df), n)]

    # 分割したデータをファイルに保存
    for i, data in enumerate(split_data):
        output_file_path = f'split_part_{i + 1}.txt'
        data.to_csv(output_file_path, sep='\t', header=False, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_file_pandas.py <file_path> <N>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2])

    split_file(file_path, n)

#python 16.py popular-names.txt 556  556行ずつ分割する場合(5分割)