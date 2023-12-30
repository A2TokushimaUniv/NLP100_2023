import subprocess
import pandas as pd
import os
from glob import glob
import shutil


def split_chunk(df, split_num, out_folder_path):
    split_length = len(df) // split_num
    for i in range(split_num):
        chunk_df = df.iloc[i * split_length : (i + 1) * split_length]
        out_file_path = f"{out_folder_path}/chunk_{i}.txt"
        chunk_df.to_csv(out_file_path, sep="\t", header=False, index=False)

    if len(df) % split_num == 0:
        return split_num, split_length

    # splitコマンドでも割り切れない時は、余りがもう一つのファイルになって出力されるのでそれに合わせる
    chunk_df = df.iloc[split_num * split_length :]
    out_file_path = f"{out_folder_path}/chunk_{split_num}.txt"
    chunk_df.to_csv(out_file_path, sep="\t", header=False, index=False)

    return split_num + 1, split_length


def test_ファイルをN分割する():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_folder_path = "./nlp100/ch02/tmp"
    os.makedirs(out_folder_path, exist_ok=True)

    split_num = 3

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    chunk_num, split_length = split_chunk(df, split_num, out_folder_path)

    command = f"split -l {split_length} {file_path} {out_folder_path}/split_"
    subprocess.run(command, shell=True, capture_output=True, text=True)

    chunk_files = glob(f"{out_folder_path}/chunk_*")
    split_files = glob(f"{out_folder_path}/split_*")

    assert len(chunk_files) == chunk_num and len(split_files) == chunk_num

    # 内容の検証
    for i, (chunk_file, split_file) in enumerate(zip(chunk_files, split_files)):
        chunk_df = pd.read_csv(chunk_file, delimiter="\t", header=None)
        split_df = pd.read_csv(split_file, delimiter="\t", header=None)

        assert chunk_df.equals(split_df)

    shutil.rmtree(out_folder_path)
