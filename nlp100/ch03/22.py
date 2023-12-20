from df import ans

ans = [a.replace('[[Category:', '').replace('|*', '').replace(']','') for a in ans]
print(ans)
