n = 10
with open("./popular-names.txt","r") as f:
    lines = f.readlines()

num = len(lines)
part_num = num//n

for i,idx in enumerate(range(0,num,part_num)):
    text = "".join(lines[idx:idx+part_num])
    out_path = "./splited/splited" + str(i+1) + ".text"
    with open(out_path,"w") as f_out:
        f_out.write(text)