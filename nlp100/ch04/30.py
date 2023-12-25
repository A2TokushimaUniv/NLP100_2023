with open("./neko.txt","r") as f:
    for line in f.readlines()[-10:]:
        print(line)