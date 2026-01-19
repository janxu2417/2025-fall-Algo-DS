# Assignment #7: 矩阵、队列、贪心

Updated 1315 GMT+8 Oct 21, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M12560: 生存游戏

matrices, http://cs101.openjudge.cn/pctbook/M12560/

思路：

周围加一圈‘0’作为保护，check函数计算每个细胞周围的活细胞数量

代码

```python
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
def check(x, y, a):
    tot = 0
    for i in range(8):
        tot += a[x + dx[i]][y + dy[i]]
    return tot

n, m = map(int, input().split())
a = [[0] * (m + 2)]
for i in range(n):
    a.append([0] + list(map(int, input().split())) + [0])
a.append([0] * (m + 2))
ans = [[0] * m for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        num = check(i, j, a)
        if a[i][j]:
            if num == 2 or num == 3: ans[i - 1][j - 1] = 1
            else: ans[i - 1][j - 1] = 0
        else: ans[i - 1][j - 1] = 1 if num == 3 else 0
for i in range(n):
    print(*ans[i])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### M04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/pctbook/M04133/

思路：

a 数组记录每个位置能获得的贡献值，mx为所有位置的最大值，ans为$a[i][j]==mx$的位置数

代码

```python
d = int(input())
n = int(input())
a = [[0] * 1025 for _ in range(1025)]
mx = 0
for i in range(n):
    x, y, m = map(int, input().split())
    for j in range(max(0, x - d), min(1025, x + d + 1)):
        for k in range(max(0, y - d), min(1025, y + d + 1)):
            a[j][k] += m
            mx = max(mx, a[j][k])
ans = 0
for j in range(1025):
    for k in range(1025):
        if a[j][k] == mx: ans += 1
print(ans, mx, sep = ' ')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M02746: 约瑟夫问题

implementation, queue, http://cs101.openjudge.cn/pctbook/M02746/

思路：

双端队列，每次将前m-1个数弹出插入尾端，将第m个数弹出，直到只剩下一个数

代码

```python
from collections import deque
while True:
    n, m = map(int, input().split())
    if not n and not m: break
    q = deque(range(1, n + 1))
    while len(q) > 1:
        for i in range(m - 1):
            q.append(q.popleft())
        x = q.popleft()
    print(q.popleft())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M26976:摆动序列

greedy, http://cs101.openjudge.cn/pctbook/M26976/


思路：

用下标为0和1表示以i为结尾的序列最后是下降和上升时的最长长度，即可DP；
优化：down和up表示1~i的序列最后是下降和上升时的最长长度，如果$a[i - 1] < a[i]$，1.1： 1~i-1以i-1为结尾最长，直接接上即可；1.2：1~i-1不以i-1而以j为结尾，如果$a[j] >= a[i - 1]$ 则j之前的序列接到i-1上也合法；如果$a[j] < a[i - 1]$ 则$a[j] < a[i]$，j后面接上i合法。
$a[i - 1] > a[i]$ 的情况与上同理,$a[i - 1] == a[i]$不需要操作。  如此可以O(n)解决。

代码 O(n^2) 暴力DP
```python
n = int(input())
a = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
ans = 1
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]: dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        if a[j] > a[i]: dp[i][0] = max(dp[i][0], dp[j][1] + 1)
    ans = max(ans, max(dp[i][0], dp[i][1]))
print(ans)
```
优化做法：O(n)
```python
n = int(input())
a = list(map(int, input().split()))
down, up = 1, 1
for i in range(1, n):
    if a[i - 1] < a[i]: 
        up = max(up, down + 1)
    if a[i - 1] > a[i]: 
        down = max(down, up + 1)
print(max(down, up))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### T26971:分发糖果

greedy, http://cs101.openjudge.cn/pctbook/T26971/

思路：

先考虑一个孩子的rank不大于其左右的rank，则他的糖果可以只发一个；然后设每个孩子左边的连续递增长度为l，右边的连续递减长度为r，那么他的糖果数至少为max(l,r)+1

代码

```python
n = int(input())
rt = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    if rt[i] > rt[i - 1]: dp[i] = max(dp[i], dp[i - 1] + 1)
for i in range(n - 2, -1, -1):
    if rt[i] > rt[i + 1]: dp[i] = max(dp[i], dp[i + 1] + 1)
print(sum(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### 1868A. Fill in the Matrix

constructive algorithms, implementation, 1300, https://codeforces.com/problemset/problem/1868/A

思路：

先考虑n + 1 == m 的特例，构造第一行为0 ~ m - 1的顺序排列，之后每一行相对于上一行将数字依序往左移动一格，则vi依次为m - 1, 0, ..., m - 2，总的beauty为m；
再考虑m < n + 1 的情况，可以证明m列可以得到的vi最多为m-1个，则总的beauty仍最大为m，则将上述的特例的前几行复制即可。
若m > n + 1，每一列只有n个数，得到的vi不超过n,则总的beauty最大为n + 1，将特例的前几列复制即可。

代码

```python
for _ in range(int(input())):
    n, m = map(int, input().split())
    if m == 1:
        print(*[0] * (n + 1), sep = '\n')
        continue
    s = min(n + 1, m)
    print(s)
    ans = []
    if s == m:
        vi = list(range(m))
        for i in range(1, s):
            tmp = []
            for j in range(i, i + s):
                tmp.append(j % s)
            ans.append(tmp)
        for i in range(n - s + 1):
            ans.append(ans[i % s])
    else:
        for i in range(1, s):
            tmp = []
            for j in range(i, i + s):
                tmp.append(j % s)
            tmp.extend(list(range(s, m)))
            ans.append(tmp)
    for i in range(n):
        print(*ans[i])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

摆动序列这道题的优化思想很有启发：dp记录以第i个数结尾的最大长度，greedy只处理前i个数的最大长度，同时由于‘摆动’的特性可以使down,up的状态转移有效（如果是单调递增就不行）。
Fill in the Matrix 这道构造题可以先处理特例，然后再考虑一般情况，冗余的行和列将特例复制即可。



