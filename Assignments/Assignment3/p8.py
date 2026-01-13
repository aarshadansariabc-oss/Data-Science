l = [1, 2, 4, 2, 5, 7, 1, 2]
s = set(l)
print(s)
for i in l:
    if i not in s:
        print(l)
