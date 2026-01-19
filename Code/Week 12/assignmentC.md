# Assignment #C: bfs & dp

Updated 1436 GMT+8 Nov 25, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy321迷宫最短路径

bfs, https://sunnywhy.com/sfbj/8/2/321

思路：

用pre[x][y]记录到达该位置的前一个位置，从原点开始搜索，到达右下角停止，最后由终点回溯得到路径。

代码：

```python
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque([(0, 0)])
    pre[0][0] = (0, 0)

    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0 and pre[nx][ny] == (-1, -1):
                pre[nx][ny] = (x, y)
                q.append((nx, ny))
                if nx == n - 1 and ny == m - 1:
                    return

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
pre = [[(-1, -1)] * m for _ in range(n)]

bfs()
ans = [(n, m)]
x, y = n - 1, m - 1
while x or y:
    x, y = pre[x][y][0], pre[x][y][1]
    ans.append((x + 1, y + 1))
for i in ans[::-1]:
    print(*i)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### sy324多终点迷宫问题

bfs, https://sunnywhy.com/sfbj/8/2/324

思路：

与前一道题类似，用step数组记录每个位置的最短步数

代码：

```python
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque([(0, 0)])
    step[0][0] = 0

    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0 and step[nx][ny] == -1:
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
step = [[-1] * m for _ in range(n)]

bfs()
for i in step:
    print(*i)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M02945: 拦截导弹

dp, greedy http://cs101.openjudge.cn/pctbook/M02945

思路：

用dp[i]记录以i为结尾的最长不增序列长度

代码：

```python
n = int(input())
h = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if h[j] >= h[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### 189A. Cut Ribbon

brute force/dp, 1300, https://codeforces.com/problemset/problem/189/A

思路：

每次在a,b,c当中选一个更新状态。

代码：

```python
n, a, b, c = map(int, input().split())
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in [i - a, i - b, i - c]:
        if j >= 0 and dp[j] >= 0:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)






### M01384: Piggy-Bank

dp, http://cs101.openjudge.cn/practice/01384/

思路：

完全背包，求重量为一定值时的最小货币面值

代码：

```python
for _ in range(int(input())):
    e, f = map(int, input().split())
    m = f - e
    dp = [0] + [1e10] * m
    for i in range(int(input())):
        p, w = map(int, input().split())
        for j in range(m - w + 1):
            dp[j + w] = min(dp[j + w], dp[j] + p)
    if dp[m] == 1e10:
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[m]}.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### M02766: 最大子矩阵

dp, kadane, http://cs101.openjudge.cn/pctbook/M02766

思路：

枚举上下边，对于列使用kadane算法。

代码：

```python
import sys
it = iter(sys.stdin.read().strip().split())
n = int(next(it))
a = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i].append(int(next(it)))
ans = a[0][0]
for i in range(n):
    b = [0 for k in range(n)]
    for j in range(i, n):
        tmp = 0
        for k in range(n):
            b[k] += a[j][k]
            tmp = max(b[k], tmp + b[k])
            ans = max(ans, tmp)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
作业的两道BFS题分别记录每个点的最短距离和前驱，异曲同工。
老师的讲义里总结了各种背包题很经典，从状态的枚举方向（单一和完全背包差异）到状态设置（从01到可用的剩余物品/选择数），非常细微的变动就可以高效优化算法。
练习了expedition、采药、红蓝玫瑰，做了模考的神经网络之国（用矩阵快速幂优化），涉及取模留余数可以在余数之间做状态转移；做了生理周期，学习了扩展欧几里得算法求逆（logn算法，可以考虑出一道加强版）




