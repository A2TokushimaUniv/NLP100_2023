import subprocess
import pandas as pd


def test_各行の1コラム目の文字列の出現頻度を求め_出現頻度の高い順に並べる():
    file_path = "./nlp100/ch02/popular-names.txt"

    df = pd.read_csv(file_path, delimiter="\t", header=None)

    name_count_df = df[0].value_counts()
    sorted_names = name_count_df.index.to_list()
    sorted_count = name_count_df.values.astype(dtype=str).tolist()

    uniq_count_command = f"cut -f 1 {file_path} | sort | uniq -c"
    to_tsv_command = "sed -e 's/  */\t/g' | cut -c 2-"  # uniqのカウントの余計なスペースを消す
    sort_command = "sort -r -n -k 1"
    get_count_command = "cut -f 1"
    command = "|".join(
        [uniq_count_command, to_tsv_command, sort_command, get_count_command]
    )
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # sortコマンドと合わなくてもいいらしいが、カウントだけでもソートされているかを確認する
    assert "\n".join(sorted_count) + "\n" == result.stdout
