import subprocess
import pandas as pd


def test_各行を3コラム目の数値の降順にソート():
    file_path = "./nlp100/ch02/popular-names.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    sorted_df: pd.DataFrame = df.sort_values(df.columns[2], ascending=False)
    sorted_column = sorted_df[2].to_csv(sep=" ", header=False, index=False)

    command = f"sort -r -n -k 3 {file_path} | cut -f 3"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # sortコマンドと合わなくてもいいらしいが、3列目だけでもソートされているかを確認する
    assert sorted_column == result.stdout
