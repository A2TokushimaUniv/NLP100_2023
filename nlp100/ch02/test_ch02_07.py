import subprocess
import pandas as pd


def test_１列目の文字列の異なり():
    file_path = "./nlp100/ch02/popular-names.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    unique_names = df[0].unique().tolist()
    unique_names.sort()

    command = f"cut -f 1 {file_path} | sort | uniq"  # uniq は sortしないと正しく機能しない
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert "\n".join(unique_names) + "\n" == result.stdout
