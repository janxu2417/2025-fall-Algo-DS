from collections import deque

h=[]
d=[[1, 0],[-1, 0],[0, 1],[0, -1]]
r,c=map(int,input().split())
in_queue = set()

def check(i, j):
    for k in range(4):
        x, y = i + d[k][0], j + d[k][1]
        if x < 0 or x > r - 1 or y < 0 or y > c - 1: continue
        if h[x][y] > h[i][j] and (x, y) not in in_queue: return 0
    return 1

def bfs():
    q = deque()
    dp=[[1] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            flag=1
            for k in range(4):
                x,y=i+d[k][0],j+d[k][1]
                if x < 0 or x > r - 1 or y < 0 or y > c - 1: continue
                if h[x][y] > h[i][j]: flag = 0
            if flag:
                q.append((i, j))
                in_queue.add((i, j))
    ans = 1
    while q:
        i,j=q.popleft()
        for k in range(4):
            x, y = i + d[k][0], j + d[k][1]
            if x < 0 or x > r - 1 or y < 0 or y > c - 1: continue
            if h[x][y] < h[i][j] and dp[x][y] < dp[i][j] + 1:
                    dp[x][y] = dp[i][j] + 1
                    if not check(x, y): continue
                    q.append((x, y))
                    in_queue.add((x, y))
                    ans = max(ans, dp[x][y])
    return ans

for i in range(r):
    h.append(list(map(int,input().split())))

print(bfs())