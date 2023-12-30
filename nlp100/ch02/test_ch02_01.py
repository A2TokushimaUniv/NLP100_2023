import subprocess
import os
import pandas as pd


def test_タブをスペースに置換():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_file_path = "./nlp100/ch02/out.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    df.to_csv(out_file_path, sep=" ", header=False, index=False)

    with open(out_file_path, mode="r", encoding="utf8") as f:
        csv_text = f.read()

    command = f"expand -t 1 {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    assert csv_text == result.stdout

    os.remove(out_file_path)
