with open("./col1.txt","r") as f_col1,open("./col2.txt","r") as f_col2:
    col1 = f_col1.read().split("\n")
    col2 = f_col2.read().split("\n")

new_text = [c1 + "\t" + c2 for c1,c2 in zip(col1,col2)]
new_text = "\n".join(new_text)
with open("./merged.text","w") as f_out:
    f_out.write(new_text)