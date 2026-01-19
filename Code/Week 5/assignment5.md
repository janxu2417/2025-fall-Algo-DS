# Assignment #5: 20251009 cs101 Mock Exam寒露第二天

Updated 1651 GMT+8 Oct 10, 2025

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

### E29895: 分解因数

implementation, http://cs101.openjudge.cn/practice/29895/



思路：

较大的因数可以由原数与较小的因数相除得到，枚举小因数又可以在$\sqrt{n}$的范围里得到

代码

```python
n = int(input())
i = 2
while i * i <= n:
    if n % i == 0:
        print(n // i)
        break
    i += 1


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)



### E29940: 机器猫斗恶龙

greedy, http://cs101.openjudge.cn/practice/29940/



思路：

假设开始血量为零，模拟整个过程，得出可能的最低血量mn，则为使实际血量大于等于1，需要初始血量为$1-mn$

代码

```python
n = int(input())
a = list(map(int, input().split()))
x = 0
mn = 0
for i in a:
    x += i
    mn = min(mn, x)
print(1 - mn)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-1.png)



### M29917: 牛顿迭代法

implementation, http://cs101.openjudge.cn/practice/29917/



思路：

模拟实现，输入用float

代码

```python
while True:
    try:
        n = float(input())
        num = 1
        x = 1.0
        y = x - (x ** 2 - n) / (2 * x)
        while abs(y - x) > 10**(-6):
            x, y = y, y - (y ** 2 - n) / (2 * y)
            num += 1
        print(f'{num} {x:.2f}')
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M29949: 贪婪的哥布林

greedy, http://cs101.openjudge.cn/practice/29949/


思路：

按照${vi}/{wi}$的大小逆序排序，优先选前面的矿石，尽可能把背包装满

代码

```python
n, m = map(int, input().split())
a = []
for _ in range(n):
    vi, wi = map(int, input().split())
    a.append((vi, wi))
a.sort(key = lambda x : x[0] / x[1], reverse = True)
ans = 0.0
for x in a:
    if m <= x[1]:
        ans += x[0] * m / x[1]
        break
    else:
        m -= x[1]
        ans += x[0]
print(f'{ans:.2f}')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M29918: 求亲和数

implementation, http://cs101.openjudge.cn/practice/29918/



思路：

对于2到n的每个数i，乘以每个小于等于i的数j，得到${i}\times{j} <= {n}$，将i和j加入乘积的因数和中（除非i == j）

代码

```python
n = int(input())
dic = [1] * (n + 1)
for i in range(2, n + 1):
    for j in range(2, i + 1):
        if j * i > n: break
        dic[j * i] += j + i * (i != j)

for i in range(220, n + 1):
    j = dic[i]
    if n >= j > i and i == dic[j]:
        print(f'{i} {j}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### T29947:校门外的树又来了（选做）

http://cs101.openjudge.cn/practice/29947/



思路：

先按左端点排序，再维护一个‘窗口’的左右端点lf，rt，如果$li <= rt + 1$就用ri去更新窗口的右端点rt，否则就新开一段窗口。

代码

```python
L, M = map(int, input().split())
a = []
for _ in range(M):
    li, ri = map(int, input().split())
    a.append((li, ri))
a.sort(key = lambda x : x[0])
j, ans = 1, 0
lf, rt = a[0][0], a[0][1]
while j < M:
    if a[j][0] <= rt + 1:
        rt = max(rt, a[j][1])
    else:
        ans += rt - lf + 1
        lf, rt = a[j][0], a[j][1]
    j += 1
ans += rt - lf + 1
print(L + 1 - ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
练习了几道dp题目（27217合法出栈顺序数的tag应该加上dp、catalan数），基本上以实现和一点贪心为主，没有特别难想到的想法。
练习了几道stack,math,set的题目，被2140B 另一种分法 题解解法震惊到（2*x）；leetcode上面选的题目每次都能学到新的知识（特别是一些要求O(n)的序列处理题），对各种小而巧的基本数据类型有更深的理解




