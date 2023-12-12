with open("./popular-names.txt","r") as f:
    lines = f.readlines()

new_lines = [line.split("\t") for line in lines]
new_lines.sort(key=lambda x:int(x[2]),reverse=True)

new_lines = ["\t".join(n_line) for n_line in new_lines]
print("".join(new_lines))

