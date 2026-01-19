nums = list(map(int, input().split(',')))
n = len(nums)
st = set(nums)
ans = 0
for x in st:
    if x - 1 in st:
        continue
    y = x + 1
    L = 1
    while y in st:
        L += 1
        y += 1
    ans = max(ans, L)
print(ans)