from collections import defaultdict
n, m = map(int, input().split())
price = list(map(int, input().split()))
price.sort()
dic = defaultdict(int)
for _ in range(m):
    dic[input()] += 1
num = sorted(dic.values(), reverse = True)
q = len(num)
# min
ans_low = 0
for i in range(q):
    ans_low += price[i] * num[i]
ans_high = 0
for i in range(q):
    ans_high += price[n - 1 - i] * num[i]
print(ans_low, ans_high)