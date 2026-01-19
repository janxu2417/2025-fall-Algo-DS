from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in range(n):
        dic[a[i] - i] += 1
    ans = 0
    for i in dic.keys():
        tmp = dic[i]
        ans += tmp * (tmp - 1) // 2
    print(ans)