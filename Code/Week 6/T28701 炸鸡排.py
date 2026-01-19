n, k = map(int,input().split())
t = list(map(int, input().split()))
t.sort(reverse = True)
tot = sum(t)
j = k
for i in range(k - 1):
    if t[i] <= tot / (k - i): break
    tot -= t[i]
    j -= 1
print(f'{tot/j:.3f}')