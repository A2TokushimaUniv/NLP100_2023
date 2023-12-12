with open("./popular-names.txt","r") as f:
    col1 = ""
    col2 = ""
    for lines in f.readlines():
        col = lines.split("\t")
        col1 += col[0]
        col1 += "\n"

        col2 += col[1]
        col2 += "\n"

with open("./col1.txt","w")as f_col1:
    f_col1.write(col1)
with open("./col2.txt","w")as f_col1:
    f_col1.write(col2)