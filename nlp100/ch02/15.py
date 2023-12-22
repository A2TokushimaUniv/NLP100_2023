import sys
import pandas as pd

def display_last_n_lines(file_path, n):
    # ファイルを逆順で読み込んで、末尾のN行を取得
    df = pd.read_csv(file_path, sep='\t', header=None, engine='python')
    last_n_lines = df.iloc[-n:]

    # 末尾のN行を表示
    print(last_n_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python display_last_n_lines_pandas.py <file_path> <N>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2])

    display_last_n_lines(file_path, n)

    #python 15.py popular-names.txt 5   入力の内末尾5行だけ表示させる場合