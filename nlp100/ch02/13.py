import pandas as pd

def merge_columns(col1_file, col2_file, merged_output_file):
    # col1.txtとcol2.txtをデータフレームとして読み込む
    col1_df = pd.read_csv(col1_file, header=None, names=['col1'])
    col2_df = pd.read_csv(col2_file, header=None, names=['col2'])

    # データフレームを横方向に結合する
    merged_df = pd.concat([col1_df, col2_df], axis=1)

    # 結合したデータフレームを新しいテキストファイルに保存する
    merged_df.to_csv(merged_output_file, sep='\t', header=False, index=False)

# col1.txtとcol2.txtを結合して新しいテキストファイルを作成する
merge_columns('col1.txt', 'col2.txt', 'merged_output.txt')