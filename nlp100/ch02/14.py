import sys
import pandas as pd

def display_n_lines(file_path, n):
    df = pd.read_csv(file_path, sep='\t', header=None, nrows=n)
    print(df)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python display_n_lines_pandas.py <file_path> <N>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2])

    display_n_lines(file_path, n)

    #python 14.py popular-names.txt 5   入力の内先頭5行だけ表示させる場合