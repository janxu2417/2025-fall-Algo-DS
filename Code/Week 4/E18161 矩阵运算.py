a, b, c = [], [], []
m1, n1 = map(int, input().split())
for _ in range(m1):
    a.append(list(map(int, input().split())))
m2, n2 = map(int, input().split())
for _ in range(m2):
    b.append(list(map(int, input().split())))
m3, n3 = map(int, input().split())
for _ in range(m3):
    c.append(list(map(int, input().split())))
if n1 != m2 or m1 != m3 or n2 != n3:
    print('Error!')
else:
    for i in range(m3):
        for j in range(n3):
            for k in range(n1):
                c[i][j] += a[i][k] * b[k][j]
        print(*c[i], sep = ' ')