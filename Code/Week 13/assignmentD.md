# Assignment #D: Mock Exam下元节

Updated 1729 GMT+8 Dec 7, 2025

2025 fall, Complied by <mark>徐前 物理学院</mark>



>**说明：**
>
>1. Dec⽉考： <mark>未参加</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29945:神秘数字的宇宙旅行 

implementation, http://cs101.openjudge.cn/practice/29945

思路：

按照题意实现

代码

```python
n = int(input())
while n > 1:
    if n % 2 == 0:
        print(f'{n}/2={n//2}')
        n = n // 2
    else:
        print(f'{n}*3+1={n*3+1}')
        n = n * 3 + 1
print('End')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### E29946:删数问题

monotonic stack, greedy, http://cs101.openjudge.cn/practice/29946

思路：

维护一个单调递增栈，如果新进来的数比栈顶的数小就弹出，直到删掉的数个数达到K，否则遍历完从栈顶逐个弹出。

代码

```python
s = input().strip()
k = int(input())
stack = []
num = 0
for i in range(len(s)):
    while stack and int(stack[-1]) > int(s[i]) and num < k:
        stack.pop()
        num += 1
    stack.append(s[i])
while num < k:
    stack.pop()
    num += 1
i = 0
while stack[i] == '0' and i < len(stack) - 1:
    i += 1
print(''.join(stack[i:]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### E30091:缺德的图书馆管理员

greedy, http://cs101.openjudge.cn/practice/30091

思路：

两个同学相遇掉头，可以等效为他们交换身份，继续往前走，如此每个同学只需分两个情况往左或往右走，计算到边界的距离。最小和最大时间分别对应每个人选择离边界近和边界远的走法。

代码

```python
l = int(input())
n = int(input())
mn, mx = 0, 0
a = list(map(int, input().split()))
for i in a:
    mn = max(mn, min(i, l + 1 - i))
    mx = max(mx, max(i, l + 1 - i))
print(mn, mx)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M27371:Playfair密码

simulation，string，matrix, http://cs101.openjudge.cn/practice/27371


思路：

按照题目要求，先生成密钥矩阵，同时dic记录每个字符的行列坐标；第二步处理明文，分三种情况确定字符对；第三步encrypt加密，处理字符对并返回密文。

代码

```python
s = ''.join([chr(97 + x) for x in range(26)])
dic = {i : (-1, -1) for i in s}
key = (input() + s).replace('j','i')
matrix = [[''] * 5 for _ in range(5)]
x, y = 0, 0
for i in key:
    if dic[i] == (-1, -1):
        matrix[x][y] = i
        dic[i] = (x, y)
        y += 1
        if y == 5:
            x += 1
            y = 0
            
def encrypt(a, b):
    ax, ay = dic[a][0], dic[a][1]
    bx, by = dic[b][0], dic[b][1]
    if ax == bx:
        return matrix[ax][(ay + 1) % 5] + matrix[bx][(by + 1) % 5]
    if ay == by:
        return matrix[(ax + 1) % 5][ay] + matrix[(bx + 1) % 5][by]
    return matrix[ax][by] + matrix[bx][ay]

for _ in range(int(input())):
    word = input().replace('j','i')
    i = 0
    ans = ''
    while i < len(word):
        if i == len(word) - 1:
            ans = ans + encrypt(word[i], 'x' if word[i] != 'x' else 'q')
        elif word[i] == word[i + 1]:
            ans = ans + encrypt(word[i], 'x' if word[i] != 'x' else 'q')
        else:
            ans = ans + encrypt(word[i], word[i + 1])
            i += 1
        i += 1
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### T30201:旅行售货商问题

dp,dfs, http://cs101.openjudge.cn/practice/30201

思路：

商人走了一个环，可以将起点固定为标号为0的城市，用二进制数i的每个位的01表示每个城市是否到达过，j记录当前到达的城市，k为下一个城市，则有转移方程$dp[i | (1 << k)][k] = min{dp[i][j] + cost[j][k]}$

代码

```python
def solve():
    n = int(input())
    size = 1 << n
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    inf = float('inf')
    dp = [[inf] * n for _ in range(size)]
    dp[1][0] = 0
    for i in range(1, size, 2):
        for j in range(n):
            if dp[i][j] == inf:
                continue
            for k in range(1, n):
                if (i >> k) & 1:
                    continue
                new_mask = i | (1 << k)
                new_cost = dp[i][j] + cost[j][k]
                if dp[new_mask][k] > new_cost:
                    dp[new_mask][k] = new_cost
    ans = inf
    for i in range(1, n):
        ans = min(ans, dp[size - 1][i] + cost[i][0])
    print(ans)
if __name__ == '__main__':
    solve()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### T30204:小P的LLM推理加速

greedy, http://cs101.openjudge.cn/practice/30204

思路：

对于每个模块，只有两种选择方式：一是选若干次xi和yi的和，二是选一次xi。

所以将xi存入s数组中升序排序，同时与xi+yi的最小值d比较，首先将能耗小于d/2的单个数选完，再尽量选满能耗为d的两个数，最后如果还有剩余，尝试能否去掉一个数放入两个数，或者能否再放入一个数。

代码

```python
n, m = map(int, input().split())
inf = float('inf')
d = inf
s = []
for _ in range(n):
    x, y = map(int, input().split())
    d = min(d, x + y)
    s.append(x)
s.sort()
i = 0
ans = 0
while i < n and s[i] * 2 < d and s[i] <= m:
    m -= s[i]
    i += 1
    ans += 1
ans += m // d * 2
m %= d
if i < n and s[i] <= m:
    m -= s[i]
    i += 1
    ans += 1
if i > 0 and s[i - 1] + m >= d:
    ans += 1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。
T1、T3都是原题
T2非常坑的一个点需要处理结果含前导0的特例，自己做的时候也是没想出来直到看了同学的提示。
T4 相对麻烦，不过充分考察了字典、字符串、矩阵的各种操作，帮我很好地复习了语法。
T5 复习了状态压缩，一个重要的思想是路径是一个环，所以起点不重要；同时参考了老师同学的优化思路，学到了将主程序放进函数优化调用时间，将min max函数改成if语句。
T6 很有意思的贪心题，回退的思想相对细节较多容易错，可以采用贪心排序+枚举选择的端点位置的思路，更加简洁


