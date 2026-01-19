f = [0, 1]
d = [0]
for i in range(1, 13):
    d.append(d[-1] * 2 + 1)
for i in range(2, 13):
    mn = d[i]
    for j in range(1, i):
        mn = min(mn, f[j] * 2 + d[i - j])
    f.append(mn)
print(*f[1:], sep = '\n')