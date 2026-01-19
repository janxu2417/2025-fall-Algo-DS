from functools import cmp_to_key

n = int(input())
pairs = [i[1:-1] for i in input().split()] # ['str1', 'str2']
distances = [sum(map(int, i.split(','))) for i in pairs]
prices = list(map(int, input().split()))

def compare(x, y):
    if distances[x]*prices[y] > distances[y]*prices[x]:
        return 1
    return -1

index = list(range(n))
index.sort(key = cmp_to_key(compare))
tmp = 0.0
if n % 2: tmp = distances[index[(n - 1) // 2]] / prices[index[(n - 1) // 2]]
else: tmp = (distances[index[n // 2 - 1]] / prices[index[n // 2 - 1]] +
             distances[index[n // 2]] / prices[index[n // 2]]) / 2

index.sort(key = lambda x : prices[x])
opt = 0.0
if n % 2: opt = 1.0 * prices[index[(n-1)//2]]
else: opt = (prices[index[n // 2]] + prices[index[n // 2 - 1]]) / 2

ans = 0
for i in index:
    if prices[i] >= opt: break
    ans += (distances[i] > prices[i] * tmp)
print(ans)