n = int(input())
dic = [1] * (n + 1)
for i in range(2, n + 1):
    for j in range(2, i + 1):
        if j * i > n: break
        dic[j * i] += j + i * (i != j)

for i in range(220, n + 1):
    j = dic[i]
    if n >= j > i and i == dic[j]:
        print(f'{i} {j}')