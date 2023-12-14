# coding: UTF-8

string1 = "aceg"
string2 = "bdfh"

string12 = "".join([x + y for x,y in zip(string1,string2)])

print(string12)