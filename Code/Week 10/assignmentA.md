# Assignment #A: 递归、田忌赛马

Updated 2355 GMT+8 Nov 4, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M018160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/pctbook/M18160

思路：

每次往外走，走过的地方打标记

代码

```python
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y, n, m, a, flag):
    flag[x][y] = 1
    ans = 1
    for t in range(8):
        xn = x + dx[t]
        yn = y + dy[t]
        if xn < 0 or xn >= n or yn < 0 or yn >= m: continue
        if flag[xn][yn] or a[xn][yn] != 'W': continue
        ans += dfs(xn, yn, n, m, a, flag)
    return ans
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    flag = []
    for i in range(n):
        a.append(input())
        flag.append([0] * m)
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'W' and not flag[i][j]:
                ans = max(ans, dfs(i, j, n, m, a, flag))
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### sy134: 全排列III 中等

https://sunnywhy.com/sfbj/4/3/134

思路：

i记录当前的层数（从0开始），tmp 记录选择的数，每次挑一个没被flag标记的数加入tmp中，加一个opt记录这一层选的数，保证相同的数不会选两次；回溯时记得删除标记

代码

```python
n = int(input())
a = list(map(int, input().split()))
def dfs(i, tmp, flag, ans):
    if i == n:
        ans.append(tmp[:])
        return
    opt = set()
    for j in range(n):
        if not flag[j] and a[j] not in opt:
            flag[j] = 1
            tmp.append(a[j])
            dfs(i + 1, tmp, flag, ans)
            flag[j] = 0
            tmp.pop()
            opt.add(a[j])
    return
ans = []
flag = [0] * n
dfs(0, [], flag, ans)
for i in ans:
    print(*i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### sy136: 组合II 中等

https://sunnywhy.com/sfbj/4/3/136

给定一个长度为的序列，其中有n个互不相同的正整数，再给定一个正整数k，求从序列中任选k个的所有可能结果。

思路：

i记录当前的层数（从0开始），tmp 记录选择的数，x记录最后一个选的位置+1，则每次选位置更大的数，可以保证不重复。可以加剪枝：最多选到位置为n-k+i+1的数，为之后的循环留下k-i-1个数

代码

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
def dfs(i, x, tmp, ans):
    if i == k:
        ans.append(tmp[:])
        return
    for j in range(x, n - k + i + 1):
        tmp.append(a[j])
        dfs(i + 1, j + 1, tmp, ans)
        tmp.pop()
    return
ans = []
dfs(0, 0, [], ans)
for i in ans:
    print(*i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### sy137: 组合III 中等

https://sunnywhy.com/sfbj/4/3/137


思路：

i记录当前的层数（从0开始），tmp 记录选择的数，x记录最后一个选的位置+1，则每次选位置更大的数，可以保证不重复。多加一个opt记录这一层选的数，保证相同的数不会选两次

代码

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
def dfs(i, x, tmp, ans):
    if i == k:
        ans.append(tmp[:])
        return
    opt = set()
    for j in range(x, n - k + i + 1):
        if a[j] not in opt:
            tmp.append(a[j])
            dfs(i + 1, j + 1, tmp, ans)
            tmp.pop()
            opt.add(a[j])
    return
ans = []
dfs(0, 0, [], ans)
for i in ans:
    print(*i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M04123: 马走日

dfs, http://cs101.openjudge.cn/pctbook/M04123

思路：

按照“日”字形，逐步向外走，用flag标记已走过的地方

代码

```python
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def dfs(k, flag, x, y, n, m):
    if k == n * m:
        return 1
    ans = 0
    for t in range(8):
        xn = x + dx[t]
        yn = y + dy[t]
        if xn < 0 or xn >= n or yn < 0 or yn >= m: continue
        if flag[xn][yn]: continue
        flag[xn][yn] = 1
        ans += dfs(k + 1, flag, xn, yn, n, m)
        flag[xn][yn] = 0
    return ans
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    flag = [[0] * m for i in range(n)]
    flag[x][y] = 1
    print(dfs(1, flag, x, y, n, m))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### T02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/pctbook/T02287

思路：

参考二分图最大匹配的匈牙利算法，先把权重为2的边跑完，然后尝试‘反悔’，看能否加进一条权重为2的边，同时只退回1权重；最后把权重为1的边跑完。

通过分析代码可以得出简化方法（也就是题解的做法）：
如果田j对王i,田k对王i+1是一组解(j小于k)，那么田k-1对王i,田k对王i+1也是一组解（且不会变差），而且对于1~i-1,i+1~n的王马来说甚至有更多选择，所以后者更好。
故最优情况只能出现在以下情况中：
i.  田1对王1，田2对王2，田3对王3......
ii. 田2对王1，田3对王2，田4对王3......
iii.田3对王1，田4对王2，田5对王3......
iv. ......

代码

```python
import sys
import bisect
data = sys.stdin.read().strip().split()
it = iter(data)
def cmp(x, y):
    if x > y: return 400
    if x == y: return 200
    return 0
while True:
    n = int(next(it))
    if not n: break
    a = []
    b = []
    for i in range(n):
        a.append(int(next(it)))
    for i in range(n):
        b.append(int(next(it)))
    a.sort()
    b.sort()
    i = j = 0
    a_to = [-1] * n
    b_to = [-1] * n
    ans = 0
    while i < n:
        while j < n and a[j] <= b[i]:
            j += 1
        if j >= n: break
        a_to[j] = i
        b_to[i] = j
        ans += 400
        i += 1
        j += 1
    # try to regret +1 edge
    if i >= 1:
        j = b_to[i - 1]
        while 1 <= i < n and a[j] > b[i]:
            tmp = 400
            for t in range(1, i + 1):
                tmp = tmp - cmp(a[b_to[i - t]],b[i - t]) + cmp(a[j - t], b[i - t])
                if a_to[j - t] == -1 or tmp <= 0: break
            if tmp <= 0: break
            for t in range(1, i + 1):
                b_to[i - t] = j - t
                if a_to[j - t] == -1:
                    a_to[j - t] = i - t
                    break
                a_to[j - t] = i - t
            a_to[j] = i
            b_to[i] = j
            ans += tmp
            i += 1
        
    if i < n: j = bisect.bisect_left(a, b[i]) 
    while i < n:
        while j < n and (a[j] < b[i] or a_to[j] > 0):
            j += 1
        if j >= n: break
        a_to[j] = i
        b_to[i] = j
        ans += 200
        i += 1
        j += 1
    print(ans - 200 * n)

    

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

田忌赛马这道题一开始跟着题目提示走，参考二分图最大匹配的匈牙利算法，先把权重为2的边跑完，然后尝试‘反悔’，看能否加进一条权重为2的边，同时只退回1权重；最后把权重为1的边跑完。最后费了一番功夫成功完成。

不过这道题的边权只有三种情况，就为贪心提供了空间（不过并不是那么好想）；从暴力到贪心的过程也让我对如何得出贪心解法有了更深刻的认识，能够较为严谨地分析贪心的正确性。


