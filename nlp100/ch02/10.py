with open('popular-names.txt')as text:
    lines = sum(1 for line in text)

    print(lines)