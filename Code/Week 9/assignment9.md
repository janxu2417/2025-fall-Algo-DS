# Assignment #9: Mock Exam立冬前一天

Updated 1658 GMT+8 Nov 6, 2025

2025 fall, Complied by <mark>物理学院 徐前</mark>



>**说明：**
>
>1. Nov⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29982:一种等价类划分问题

hashing, http://cs101.openjudge.cn/practice/29982

思路：

利用字典哈希实现，开始字典的key没有排序被坑了好久。。。

代码

```python
from collections import defaultdict

def sol(x):
    y = 0
    while x > 0:
        y += x % 10
        x //= 10
    return y

m, n, k = map(int, input().split(','))
dic = defaultdict(list)
for i in range(m + 1, n):
    x = sol(i)
    if x % k == 0:
        dic[x].append(str(i))
for i in sorted(dic.keys()):
    print(','.join(dic[i]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### E30086:dance

greedy, http://cs101.openjudge.cn/practice/30086

思路：

顺序排序，高度最小者优先与次小者结对，如果不行那么更高的人更不可能实现。

代码

```python
n, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
flag = 0
for i in range(n):
    if a[2 * i + 1] - a[2 * i] > d:
        flag = 1
        break
print('Yes' if flag == 0 else 'No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### M25570: 洋葱

matrices, http://cs101.openjudge.cn/practice/25570

思路：

以到边界的距离为序号统计分组。

代码

```python
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
cnt = [0] * n
for i in range(n):
    for j in range(n):
        x = min(min(i, n - 1 - i), min(j, n - 1 - j))n
        cnt[x] += a[i][j]
print(max(cnt))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M28906:数的划分

dfs, dp, http://cs101.openjudge.cn/practice/28906


思路：

dp[i][j][k] 表示i分成k个数，最大数不超过j的方案数，则得到转移方程dp[i][j][k] = dp[i][j - 1][k] + dp[i - j][j][k-1]，注意到每次由k-1向k转移，dp不需要存储之前的状态值，只需每次初始化dp[i][0]为0，枚举i时从大到小，那么dp[i][j]即为分成k个数的方案数，dp[i-j][j]为分成k-1个数的方案数。
小优化：j需要小于等于i-k+1才又可能实现（前面有k-1个1），同理，i-j需要最大数不超过i-j-k+2
总复杂度O(k*n^2)

代码

```python
n, m = map(int, input().split())
dp = [[0]]
for i in range(1, n + 1):
    dp.append([0 for j in range(i + 1)])
    dp[i][i] += 1

for k in range(2, m + 1):
    for i in range(n, k - 1, -1):
        dp[i][0] = 0
        for j in range(1, i - k + 2):
            dp[i][j] = dp[i][j - 1] + dp[i - j][min(j, i - j - k + 2)]
            #for t in range(max(1, (i - j) // k), min(j + 1, i - j - k + 3)):
            #    dp[i][j][k % 2] += dp[i - j][t][(k + 1) % 2]

print(dp[n][n - m + 1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M29896:购物

greedy, http://cs101.openjudge.cn/practice/29896

思路：

从小到大排序，前i-1个硬币应该需要排出1~a[i]-1的所有面值，如果不够，就加一个a[i-1]的硬币。

最后注意是上取整！！！

代码

```python
x, n = map(int, input().split())
a = sorted(list(map(int, input().split())))
if a[0] != 1:
    print(-1)
else:
    tmp = 1
    ans = 1
    for i in range(1, n):
        while tmp < a[i] - 1 and tmp < x:
            tmp += a[i - 1]
            ans += 1
    if tmp < x: ans += (x - tmp + a[n - 1] - 1) // a[n - 1]
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### T25353:排队

greedy, http://cs101.openjudge.cn/practice/25353

思路：

贪心：字典序最小必要第一位上最小；同时注意到有类似图的“联通”性质——与最高mx和最低mn距离都不超过d的同学可以移到最前面——将这些人放入tmp数组，进行sort排序。
每次需要把放入tmp数组的人从待选列表中去除，用链表可以实现，去除只需把i的pre连到i的next上即可。
学习了同学的优化想法以后，可以把每次更新的tmp数组按指标存储，从前往后依次表示每个等价类，mx,mn数组存储每个等价类的最大值最小值。这样就可以一次遍历整个数组，找每个元素所属的等价类

代码1

链表优化改进了OOP写法

```python
class Node:
    def __init__(self, value, idx):
        self.value = value
        self.pre = idx - 1
        self.next = idx + 1

class LinkedList:
    def __init__(self, n):
        self.nodes = []
        #h = list(map(int, input().split()))
        for i in range(n):
            val = int(input())
            self.nodes.append(Node(val, i))
        self.start = 0
        self.tail = n

    def remove(self, idx):
        node = self.nodes[idx]
        if idx == self.start:
            self.start = node.next
        else:
            self.nodes[node.pre].next = node.next
            if node.next == self.tail:
                self.tail = idx
            else:
                self.nodes[node.next].pre = node.pre

    def solve(self, d):
        ans = []
        while self.start != self.tail:
            tmp = []
            i = self.start
            mn = mx = self.nodes[i].value

            while i != self.tail:
                x = self.nodes[i].value
                nxt = self.nodes[i].next
                if mx - d <= x <= mn + d:
                    tmp.append(x)
                    self.remove(i)

                mn = min(mn, x)
                mx = max(mx, x)
                if mx - mn > 2 * d:
                    break
                i = nxt

            ans.extend(sorted(tmp))

        return ans

# main
n, d = map(int, input().split())
q = LinkedList(n)
result = q.solve(d)

print(*result, sep='\n')
```

**排队又来了**

运用等价类思想（借鉴了同学的做法），将整个数组划分成若干个等价类，每个等价类内的数可以互相交换，但是都无法换到前面的等价类中。用mns,mxs记录每个等价类的最小和最大值（由定义可得mxs[i]-mns[i]<=d）
顺序遍历每个数，去找它能到达的最前面的等价类，如果没有一个类能容纳，则新建一个等价类。


```python
n, d = map(int, input().split())
h = list(map(int, input().split()))
q = [[h[0]]]
mns = [h[0]]
mxs = [h[0]]
for i in range(1, n):
    x = h[i]
    if mxs[-1] - d > x or x > mns[-1] + d:
        q.append([x])
        mns.append(x)
        mxs.append(x)
    else: #mxs[-1] - d <= x <= mns[-1] + d:
        j = len(q) - 1
        while j >= 0 and mxs[j] - d <= x <= mns[j] + d:
            j -= 1
        q[j + 1].append(x)
        mns[j + 1] = min(mns[j + 1], x)
        mxs[j + 1] = max(mxs[j + 1], x)
ans = []
for i in q:
    ans.extend(sorted(i))
print(*ans)
```


代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。

这次自己计时，难点还是有思路以后代码的debug：

T1、dict的keys并不是按照大小排序的，需要sorted以后输出
T5、最后没注意用最大硬币补足x的差值是上取整
数的划分可以利用前缀和思想，排队要充分利用等价的思想。



