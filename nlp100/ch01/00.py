# conda create –n nlp100（「nlp100」という名前の仮想環境作成）
# conda activate nlp100（仮想環境アクティブ化）
# conda install python=3.10.12（Pythonのインストール）
# conda deactivate（仮想環境⾮アクティブ化）

# 00. 文字列の逆順Permalink
# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
text = "stressed"
print(text[::-1])