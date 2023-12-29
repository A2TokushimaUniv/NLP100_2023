import subprocess
import pandas as pd

def test_行数のカウント():
    file_path = "./nlp100/ch02/popular-names.txt"
    df = pd.read_csv(file_path, delimiter='\t', header=None)
    command = f"wc {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    line_num = result.stdout.split(" ")[1]
    assert len(df) == int(line_num)
