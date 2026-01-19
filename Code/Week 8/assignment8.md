# Assignment #8: 递归

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

### M04147汉诺塔问题(Tower of Hanoi)

dfs, http://cs101.openjudge.cn/pctbook/M04147

思路：



代码

```python
def dfs(n, a, b, c):
    if n == 1:
        print(f'1:{a}->{c}')
        return
    dfs(n - 1, a, c, b)
    print(f'{n}:{a}->{c}')
    dfs(n - 1, b, a, c)
    return
s = input().split()
n = int(s[0])
a, b, c = s[1], s[2], s[3]
dfs(n, a, b, c)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M05585: 晶矿的个数

matrices, dfs similar, http://cs101.openjudge.cn/pctbook/M05585

思路：

用flag数组记录每个点是否被访问过，然后对于红矿和黑矿所在点dfs，向四个方向扩展，访问到的点令flag为1，不重复访问。

代码

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, n, m, flag, c):
    for k in range(4):
        x1, y1 = x + dx[k], y + dy[k]
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n: continue
        if m[x1][y1] != c or flag[x1][y1]: continue
        flag[x1][y1] = 1
        dfs(x1, y1, n, m, flag, c)
    return
for _ in range(int(input())):
    n = int(input())
    m = []
    for i in range(n):
        m.append(input())
    ans = [0, 0]
    flag = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] != '#' and not flag[i][j]:
                flag[i][j] = 1
                dfs(i, j, n, m, flag, m[i][j])
                if m[i][j] == 'r' : ans[0] += 1
                else : ans[1] += 1
    print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M02786: Pell数列

dfs, dp, http://cs101.openjudge.cn/pctbook/M02786/

思路：

按题意实现即可

代码

```python
n=int(input())
a=[0,1,2]
mod=32767
for i in range(3,10**6):
    a.append((2*a[i-1]+a[i-2])%mod)
while n:
    k=int(input())
    print(a[k])
    n-=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M46.全排列

backtracking, https://leetcode.cn/problems/permutations/


思路：

flag 数组记录每个数有没有用过，tmp 数组记录当前选好的排列，每次在剩下的flag 为0的数当中选一个加入 tmp 中，递归进入下一层，递归完以后删除。
注意 整个dfs中tmp只有一个地址，如果ans.append(tmp)则是拷贝一个地址（浅拷贝），最后全是$[[],[],[]]$，深拷贝需要ans.append(tmp[:]) 

代码

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, n, flag, tmp, nums, ans):
            if i == n:
                ans.append(tmp[:])
                return
            for j in range(n):
                if not flag[j]:
                    flag[j] = 1
                    tmp.append(nums[j])
                    dfs(i + 1, n, flag, tmp, nums, ans)
                    flag[j] = 0
                    tmp.pop()
        n = len(nums)
        flag = [0] * n
        tmp = []
        ans = []
        dfs(0, n, flag, tmp, nums, ans)
        return ans
if __name__ == '__main__':
    nums = list(map(int, input().split()))
    solution = Solution()
    res = solution.permute(nums)
    print(res)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### T02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/pctbook/T02754

思路：

flag 数组记录每个数有没有用过， s 字符串记录当前选好的排列，每次在剩下的flag 为0的数当中，用check函数判断斜方向有无重合，选一个不重合的加入 s 中，递归进入下一层。

代码

```python
def check(x, s):
    for k in range(len(s)):
        if abs(int(s[k]) - x) == len(s) - k: return False
    return True
def dfs(i, n, s, flag, ans):
    if i == n:
        ans.append(s[:])
        return
    for j in range(1, n + 1):
        if not flag[j] and check(j, s):
            flag[j] = 1
            dfs(i + 1, n, s + str(j), flag, ans)
            flag[j] = 0
    return
ans = []
flag = [0] * 9
dfs(0, 8, '', flag, ans)
for _ in range(int(input())):
    print(ans[int(input()) - 1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### T01958 Strange Towers of Hanoi

http://cs101.openjudge.cn/practice/01958/

思路：

用d数组存三柱汉诺塔的步数，f数组存Strange汉诺塔的步数，则用分治思想：先将上面j个盘子移到中间的柱子上（四柱问题），再把i-j个盘子移到目标柱上（三柱问题），最后把j个盘子移到目标柱上（四柱问题）。

代码

```python
f = [0, 1]
d = [0]
for i in range(1, 13):
    d.append(d[-1] * 2 + 1)
for i in range(2, 13):
    mn = d[i]
    for j in range(1, i):
        mn = min(mn, f[j] * 2 + d[i - j])
    f.append(mn)
print(*f[1:], sep = '\n')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

递归题练习了全排列、N皇后、分割回文串、子集；额外练习了月度开销（经典二分），单调栈和kadane。

### T27205 护林员盖房子 加强版

Monotonic Stack, http://cs101.openjudge.cn/pctbook/T27205/

收获：学习了Monotonic Stack以后练习了接雨水和这道题；可以概括找出左右第一个比它大（或小）的数这样的题型。
护林员这道题可以抽象成求直方图中的最大矩形面积：通过维护一个单调递增栈，可以高效地确定每个柱子的左右边界（即左右第一个比它矮的柱子），从而计算出以该柱子为高的最大矩形面积。我觉得最妙的一点在于，将一个数弹出的时候再计算以它为高的矩形面积（这时候矩形的长刚好可以确定）只需O(n)，但如果采用遍历的方法对每个数作为左边界枚举右边界再计算矩形的高则需要O(n^2)。
具体实现：枚举行的下边界，如果是空地则将对应的柱子高度h加1，如果是树林就把h赋值为0，为了方便，可以在h数组的头和尾各放一个0。

```python
def solve(h, n):
    mx = 0
    stack = [0]
    for i in range(1, n):
        while stack and h[stack[-1]] > h[i]:
            index = stack.pop()
            l = index
            if stack: l = stack[-1] + 1
            mx = max(mx, h[index] * (i - l))
        stack.append(i)
    return mx

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
h = [0] * (n + 2)
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j]: h[j + 1] = 0
        else: h[j + 1] += 1
    ans = max(ans, solve(h, n + 2))
print(ans)
```
![alt text](image.png)



