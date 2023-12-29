import subprocess
import pandas as pd
def test_末尾のN行を出力():
    file_path = "./nlp100/ch02/popular-names.txt"
    line_num = 10

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    tail_lines = df.tail(line_num).to_csv(sep="\t",header=False, index=False)

    command = f"tail -n {line_num} {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert tail_lines == result.stdout
