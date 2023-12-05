def cipher(input):
    output = ""
    for s in input:
        if s.islower():
            output += chr(219-ord(s))
        else:
            output += s
    return output

input = "ABC abc 123"
ans = cipher(input)
print(ans)