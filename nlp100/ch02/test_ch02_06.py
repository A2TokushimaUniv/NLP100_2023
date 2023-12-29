import subprocess
import pandas as pd
import os
from glob import glob
import shutil


def test_ファイルをN分割する():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_folder_path = "./nlp100/ch02/tmp"
    os.makedirs(out_folder_path, exist_ok=True)

    split_num = 3

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    split_length = len(df) // split_num
    for i in range(split_num):
        if i < split_num - 1:
            chunk_df = df.iloc[i * split_length : (i + 1) * split_num]
        else:
            chunk_df = df.iloc[i * split_num :]

        out_file_path = f"{out_folder_path}/chunk_{i}.txt"
        chunk_df.to_csv(out_file_path, sep="\t", header=False, index=False)

    command = f"split -n {split_num} {file_path}/split_ {out_folder_path}"
    subprocess.run(command, shell=True, capture_output=True, text=True)

    chunk_files = glob(f"{out_folder_path}/chunk_*.txt")
    split_files = glob(f"{out_folder_path}/split_*.txt")

    for i, chunk_file, split_file in enumerate(zip(chunk_files, split_files)):
        chunk_df = pd.read_csv(chunk_file, delimiter="\t", header=None)
        split_df = pd.read_csv(split_file, delimiter="\t", header=None)

        assert chunk_df.equals(split_df)

    shutil.rmtree(out_folder_path)
