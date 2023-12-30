import subprocess
import pandas as pd


def test_先頭からN行を出力():
    file_path = "./nlp100/ch02/popular-names.txt"
    out_path = "./nlp100/ch02/out.txt"
    line_num = 10

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    head_lines = df.head(line_num).to_csv(sep="\t", header=False, index=False)

    command = f"head -n {line_num} {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    assert head_lines == result.stdout
