def generate_string(x, y, z):
    
    result_string = "{}jino{}ha{}".format(x, y, z)
    return result_string

x = 12
y = "kion"
z = 22.4

result = generate_string(x, y, z)
print(result)