import subprocess
import pandas as pd
import os

def test_1列目をcol1_txtに保存():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_file_path = "./nlp100/ch02/col1.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)
    col1 = df.iloc[:, 0]
    col1.to_csv(out_file_path, sep=" ", header=False, index=False)
    with open(out_file_path, mode="r", encoding="utf8") as f:
        col_text = f.read()

    command = f"cut -f 1 {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert col_text == result.stdout

    os.remove(out_file_path)


def test__2列目をcol2_txtに保存():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_file_path = "./nlp100/ch02/col2.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)
    col2 = df.iloc[:, 1]
    col2.to_csv(out_file_path, sep=" ", header=False, index=False)
    with open(out_file_path, mode="r", encoding="utf8") as f:
        col_text = f.read()

    command = f"cut -f 2 {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert col_text == result.stdout

    os.remove(out_file_path)
