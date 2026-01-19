# Assignment #6: 矩阵、贪心

Updated 1432 GMT+8 Oct 14, 2025

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

### M18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/pctbook/M18211



思路：

升序排序，用双指针，如果能买尽可能买最小的，如果买不了则卖一个最贵的，再试能不能买。

代码

```python
p = int(input())
a = list(map(int, input().split()))
n = len(a)
a.sort()
i, j = 0, n - 1
mx = 0
num = 0
while i <= j and (p >= a[i] or num):
    while i <= j and p >= a[i]:
        p -= a[i]
        num += 1
        i += 1
    mx = max(mx, num)
    if i <= j and num:
        p += a[j]
        num -= 1
        j -= 1
print(mx)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M21554: 排队做实验

greedy, http://cs101.openjudge.cn/pctbook/M21554/



思路：

时间短的先做

代码

```python
n = int(input())
t = list(map(int, input().split()))
a = []
for i in range(n):
    a.append((t[i], i + 1))
a.sort()
ans = 0
result = []
for i in range(n):
    result.append(a[i][1])
    ans += a[i][0] * (n - i - 1)
print(*result)
print(f'{ans / n:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/pctbook/E23555



思路：

dic1[i],dic2[j]里存储X矩阵第i行的非零项与Y矩阵第j行的非零项，对每个k算非零的x[i][k]*y[k][j]累加。

代码

```python
from collections import defaultdict
n, m1, m2 = map(int, input().split())
x, y = [], []
dic1 = defaultdict(list)
dic2 = defaultdict(list)
for i in range(m1):
    a, b, c = map(int, input().split())
    x.append((a, b, c))
    dic1[a].append((b, c))
for i in range(m2):
    a, b, c = map(int, input().split())
    y.append((a, b, c))
    dic2[b].append((a, c))
for j in range(n):
    if len(dic2[j]):
        dic2[j].sort()
for i in range(n):
    if len(dic1[i]):
        dic1[i].sort()
        for j in range(n):
            if len(dic2[j]):
                tmp, k, t = 0, 0, 0
                while k < len(dic1[i]) and t < len(dic2[j]):
                    if dic1[i][k][0] == dic2[j][t][0]:
                        tmp += dic1[i][k][1] * dic2[j][t][1]
                        k += 1
                        t += 1
                    elif dic1[i][k][0] < dic2[j][t][0]:
                        k += 1
                    else:
                        t += 1
                if tmp:
                    print(i, j, tmp, sep = ' ')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### M12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/pctbook/M12558


思路：

在输入数据的周围加上一圈0作为保护；找到最靠左上角的1作为起点，然后沿着边缘走一圈，始终维持在岛屿格子的左边缘

代码

```python
n, m = map(int, input().split())
a = [[0] * (m + 2)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(sx, sy, x, y, t):
    if sx == x and sy == y and t == 3:
        return 1
    xn, yn = x + d[t][0], y + d[t][1]
    if a[xn][yn] == 0: # turn right
        return dfs(sx, sy, x, y, (t + 1) % 4) + 1
    t1 = (t + 3) % 4
    xl, yl = xn + d[t1][0], yn + d[t1][1]
    if a[xl][yl] == 1: # turn left
        return dfs(sx, sy, xl, yl, t1) + 1
    # go straight
    return dfs(sx, sy, xn, yn, t) + 1
for i in range(n):
    row = [0]
    row.extend(list(map(int, input().split())))
    row.append(0)
    a.append(row)
a.append([0] * (m + 2))
flag = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j]:
            print(dfs(i, j, i, j, 0))
            flag = 1
            break
    if flag: break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### M01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：

生成每个岛屿距离小于等于d范围内的雷达满足的区间，按左端点排序，取尽可能多的区间的交集，且不为空，交集内安排一个雷达，然后新开一个区间。

代码

```python
from math import sqrt
t = 1
while True:
    n, d = map(int, input().split())
    if not n and not d: break
    a = []
    flag = 0
    for i in range(n):
        x, y = map(int, input().split())
        if y > d: flag = 1
        else:
            l = - sqrt(d ** 2 - y ** 2) + 1.0 * x
            r = sqrt(d ** 2 - y ** 2) + 1.0 * x
            a.append((l, r))
    if flag:
        print(f'Case {t}: -1')
    else:
        a.sort(key = lambda x : x[0])
        lf = a[0][0]
        rt = a[0][1]
        ans = 1
        for i in range(1, n):
            if a[i][0] <= rt:
                lf = a[i][0]
                rt = min(rt, a[i][1])
            else:
                lf = a[i][0]
                rt = a[i][1]
                ans += 1
        print(f'Case {t}: {ans}')
    _ = input()
    t += 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C



思路：

第一棵树一定往左倒，从左到右枚举第i棵树，如果它能往左倒，一定最优；
如果不能则尝试往右倒，为什么不能让它右边的树往左倒呢？因为i的树往右倒和i+1的树往左倒这两种情况（假设只能满足其一）对于更右边的树来说情况是一样的（不劣），同时前者比后者可能有更优的结果（i+1可能可以再向右倒），所以Greedy成立

代码

```python
n = int(input())
a = []
for i in range(n):
    x, h = map(int, input().split())
    a.append((x, h))
ans = 1
lf = a[0][0]
for i in range(1, n - 1):
    if lf < a[i][0] - a[i][1]:
        ans += 1
        lf = a[i][0]
    elif a[i + 1][0] > a[i][0] + a[i][1]:
        ans += 1
        lf = a[i][0] + a[i][1]
    else:
        lf = a[i][0]
if n > 1: ans += 1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

收获：这次作业的贪心题目都很经典，思路可以归结为按照某一种顺序（如区间左端点）比较相邻两个状态哪一个更优（如一个区间可以覆盖另一个区间），然后通过局部最优推出全体最优。

练习了一些每日选作中的题目：hashing: 1520D，完美立方(枚举实现)，假币问题(暴力枚举) 

### M02810: 完美立方
hashing, http://cs101.openjudge.cn/pctbook/M02810/

思路：
先枚举b和c，将其立方和存入字典的key，value存入c；然后枚举a和d，直接查询其立方差是否在字典的key中，并且value中小于等于d的c作为合法解。这样整体时间复杂度可以均摊到O(n^2)

```python
from collections import defaultdict
n = int(input())
dic = defaultdict(list)
for b in range(2, n):
    for c in range(b, n):
        dic[c ** 3 + b ** 3].append(c)
ans = []
for a in range(6, n + 1):
    for d in range(5, a):
        tmp = a ** 3 - d ** 3
        if len(dic[tmp]):
            for c in dic[tmp]:
                if c <= d:
                    b = (tmp - c ** 3) ** (1/3)
                    ans.append((a, round(b), c, d))
ans.sort()
for i in ans:
    a, b, c, d = i[0], i[1], i[2], i[3]
    print(f'Cube = {a}, Triple = ({b},{c},{d})')

```
![alt text](image-6.png)




