from collections import deque
# 约瑟夫问题 2
while True:
    n, p, m = map(int, input().split())
    if not n and not m: break
    q = deque(range(1, n + 1))
    for i in range(p - 1):
        q.append(q.popleft())
    ans = []
    while len(q) > 0:
        for i in range(m - 1):
            q.append(q.popleft())
        ans.append(q.popleft())
    print(*ans, sep=',', end='\n')
