# Assignment #2: 语法练习

Updated 1335 GMT+8 Sep 16, 2025

**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |

>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>   对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### 263A. Beautiful Matrix

implementation, 800, https://codeforces.com/problemset/problem/263/A



思路：
算出行和列数与中心的差，绝对值相加


代码

```python
import sys

data = sys.stdin.read()
lines = data.splitlines()
i = flag = j = 0
for line in lines:
    list1 = list(map(int, line.split()))
    j = 0
    for x in list1:
        if x == 1:
            flag = 1
            break
        j += 1
    if flag: break
    i += 1
print(abs(i - 2) + abs(j - 2))


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### 1328A. Divisibility Problem

math, 800, https://codeforces.com/problemset/problem/1328/A



思路：
$(b-a \mod b) \mod b$


代码

```python
t=int(input())
while t :
    a,b=map(int,input().split())
    t-=1
    print((b-a%b)%b)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### 427A. Police Recruits

implementation, 800, https://codeforces.com/problemset/problem/427/A



思路：
如果有警察在线，就处理；若没有，则答案加一


代码

```python
n = int(input())
a = list(map(int,input().split()))
cnt=ans=0
for i in a:
    if cnt+i >= 0: cnt += i
    else: ans+=1
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### E02808: 校门外的树

implementation, http://cs101.openjudge.cn/pctbook/E02808/


思路：
暴力实现，线段标记0
另一种想法：根据区间左端点排序，维持一个指针指向当前区间的最右端，若下一个区间左端点有重合，则直接跳到右端点，否则统计中间没被挖掉的树。


代码

```python
L,M = map(int,input().split())
a = [1] * (L+1)
for i in range(M):
    x,y = map(int,input().split())
    for j in range(x,y+1):
        a[j] = 0
print(a.count(1))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### sy60: 水仙花数II

implementation, https://sunnywhy.com/sfbj/3/1/60



思路：枚举，记得除掉末尾空格



代码

```python
a,b=map(int,input().split())
ans=[]
for i in range(a,b+1):
    x = i // 100
    y = i % 100 // 10
    z = i % 10
    if x**3 + y**3 + z**3 == i:
        ans.append(i)
if len(ans) == 0:
    print('NO',end='')
else:
    for i in range(len(ans)-1):
        print(ans[i],end=' ')
    print(ans[-1],end='')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### M01922: Ride to School

implementation, http://cs101.openjudge.cn/pctbook/M01922/



思路：
先找第一个出发的；然后按照速度由小到大排序，计算目前各个速度大于Charley的骑手与Charley的相遇时间，取最短者跟随之；直到在到达学校前没有人能再超越他。


代码

```python
# greedy
import math
while True:
    n = int(input())
    if not n: break
    a=[]
    for i in range(n):
        vi,ti = map(int,input().split())
        a.append((vi,ti))
    a.sort(key = lambda x : x[0])
    i=0
    v=0
    t0=-1
    for j in range(n):
        if a[j][1] >= 0 and (a[j][1] <= t0 or t0 == -1):
            v,t0 = a[j][0] , a[j][1]
            i = j
    while i < n:
        tmin=-1.0
        opt=-1
        for j in range(i+1,n):
            if a[j][0] == v : continue
            t_meet = (a[j][0]*a[j][1]-v*t0)/(a[j][0]-v)
            if t_meet < 0 : continue
            if tmin < 0 or t_meet <= tmin:
                tmin=t_meet
                opt=j
        if opt == -1 : break
        if v * (tmin - t0) >= 4.5 * 3600 : break
        v = a[opt][0]
        t0 = a[opt][1]
        i = opt
    print(math.ceil(4.5 * 3600 / v + t0))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

个人收获：解决了搜索、字符串、动态规划的一些例子，更加熟悉python中的列表list、字典dict、集合set、queue的用法，研究了一些有趣的数学思想

### M01088:滑雪

http://cs101.openjudge.cn/pctbook/M01088/

思路：宽度搜索，用dp数组存储到每个点的最大的长度。一个点进队当且仅当高度大于等于它的点已全部进队，每个点只会进过一次队，保证$O(rc)$的复杂度


代码

``` python

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
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)


### 1366D:two dividers

https://codeforces.com/contest/1366/problem/D

思路：设$x=a\times b$，且$gcd(a, b) = 1$则可以证明$gcd(a+b,x)=1$，则一种构造方式是找到x的一个质因数，并将其完全除去。只当x只有一个质因数时，无法构造

```c++
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> prm;
vector<bool> is_prm(3170, true);
vector<int> d1, d2;
unordered_map<int, pair<int, int>> dic;

void divide(int x) {
    int y = x;
    bool flag = false;
    // 检查是否已经计算过
    if (dic.find(x) != dic.end()) {
        d1.push_back(dic[x].first);
        d2.push_back(dic[x].second);
        return;
    }
    
    // 尝试分解质因数
    for (int i : prm) {
        if (i * i > x) break;
        if (y % i == 0) {
            int tmp = 1;
            while (y % i == 0) {
                y /= i;
                tmp *= i;
            }
            if (tmp == x) continue;
            dic[x] = make_pair(tmp, x / tmp);
            d1.push_back(tmp);
            d2.push_back(x / tmp);
            flag = true;
            break;
        }
    }
    // 如果无法分解，标记为-1,-1
    if (!flag) {
        dic[x] = make_pair(-1, -1);
        d1.push_back(-1);
        d2.push_back(-1);
    }
}

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) 
        cin >> a[i];
    
    // 生成质数表（埃拉托斯特尼筛法）
    for (int i = 2; i < 3170; ++i) {
        if (is_prm[i]) {
            prm.push_back(i);
        }
        for (int j : prm) {
            if (i * j >= 3170) break;
            is_prm[i * j] = false;
            if (i % j == 0) break;
        }
    }
    
    for (int x : a)
        divide(x);
    
    for (int i : d1)
        cout << i << " ";
    cout << endl;
    
    for (int i : d2)
        cout << i << " ";
    return 0;
}

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-7.png)
