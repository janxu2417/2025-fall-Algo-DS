n = int(input())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
index = list(range(n))
index.sort(key = lambda x : a[x])
ans = 'Poor'
for i in range(n - 1):
    if b[index[i]] > b[index[i + 1]]:
        ans = 'Happy'
        break
print(' '.join([ans,'Alex']))