with open("./popular-names.txt","r") as f:
    new_lines = [line.replace("\t"," ") for line in f.readlines()]
    new_lines = "".join(new_lines)
    print(new_lines)