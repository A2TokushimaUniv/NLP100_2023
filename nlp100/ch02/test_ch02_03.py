import subprocess
import os
import pandas as pd
import shutil


def split_col(df, col_idx, out_file_path):
    col = df.iloc[:, col_idx]
    col.to_csv(out_file_path, sep=" ", header=False, index=False)
    return col


def test_col1_txtとcol2_txtをマージ():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_folder_path = "./nlp100/ch02/tmp"
    col1_file_path = f"{out_folder_path}/col1.txt"
    col2_file_path = f"{out_folder_path}/col2.txt"
    out_file_path = f"{out_folder_path}/out.txt"

    os.makedirs(out_folder_path, exist_ok=True)

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    col1 = split_col(df, 0, col1_file_path)
    col2 = split_col(df, 1, col2_file_path)

    col_1_2 = pd.concat((col1, col2), axis=1)
    col_1_2.to_csv(out_file_path, sep="\t", header=False, index=False)
    with open(out_file_path, mode="r", encoding="utf8") as f:
        col_1_2_text = f.read()

    command = f"paste {col1_file_path} {col2_file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    assert col_1_2_text == result.stdout

    shutil.rmtree(out_folder_path)
