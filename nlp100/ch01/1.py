sentence = "パタトクカシーー"

numbers = [1, 3, 5, 7]

result = ""
for num in numbers:
    result += sentence[num - 1]
print(result)
