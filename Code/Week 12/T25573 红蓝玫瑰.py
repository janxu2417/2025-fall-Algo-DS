s = input()
r, g = 0, 0
for i in s:
    if i == 'R':
        g = min(r + 1, g + 1)
    else:
        r = min(r + 1, g + 1)
print(r)