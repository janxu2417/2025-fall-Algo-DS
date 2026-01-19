s = list(input().strip(';').split(';'))
a, b, c = 0, 0, 0
for si in s:
    p = si[0]
    x = int(si[-1])
    if p == 'a': a = x
    elif p == 'b': b = x
    else: c = x
print(a, b, c)