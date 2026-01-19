# Assignment #1: 自主学习

Updated 1626 GMT+8 Sep 19, 2025

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
>4. **延迟提交：****如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E02733: 判断闰年

http://cs101.openjudge.cn/pctbook/E02733/



思路：
根据$mod 4、100、400$是否为0，分类讨论


代码

```python
# 
a=int(input())
if a%4!=0:
    print('N')
else:
    if a%100!=0:
        print('Y')
    else:
        if a%400!=0:
            print('N')
        else:
            print('Y')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](E02733.jpeg)




### E02750: 鸡兔同笼

http://cs101.openjudge.cn/pctbook/E02750/



思路：
鸡的最大可能数量为$n/2$向下取整，从0到n枚举鸡的数量，判断能否满足兔子的数量为正整数。


代码

```python
# 
a=int(input())
n=a//2 #鸡的最大可能数量
min,max=0,0
for i in range(0,n+1):
    if not (a-i*2)%4:
        tot=i+(a-i*2)//4
        if tot<min or not min:
            min=tot
        if tot>max:
            max=tot
print(min,max)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](E02750.jpeg)




### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：
贪心，有偶数行或列就可以摆满，若均为奇数，则刨除角落的一块无法覆盖，其余均可覆盖。


代码

```python
# 
n,m=map(int,input().split())
if n%2==0 or m%2==0:
    print(n*m//2)
else:
    print((n*m-1)//2)

```
![alt text](屏幕截图_12-9-2025_19131_codeforces.com.jpeg)


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：
$n/a$和$m/a$向上取整后，相乘


代码

```python
# 
def divide_up(n,a):
    return (n+a-1)//a

n,m,a=map(int,input().split())
print(divide_up(n,a)*divide_up(m,a))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](屏幕截图_12-9-2025_19036_codeforces.com.jpeg)




### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：
$a$的ASCII码为65，$A$的ASCII码为97


代码

```python
# 
s1=input()
s2=input()
ans=0
for i in range(len(s1)):
    x1=ord(s1[i])
    x2=ord(s2[i])
    if x1>=97:
        x1=x1-97+65
    if x2>=97:
        x2=x2-97+65
    if x1<x2:
        ans=-1
        break
    if x2<x1:
        ans=1
        break
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](屏幕截图_12-9-2025_19927_codeforces.com.jpeg)




### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：
朴素无华


代码

```python
# 
n=int(input())
ans=0
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        ans+=1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](屏幕截图_12-9-2025_19927_codeforces.com-1.jpeg)




## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。==

### M03143.验证“歌德巴赫猜想”

http://cs101.openjudge.cn/pctbook/M03143/

思路：结合欧拉筛素数的方法，只用枚举比y/2小的素数。

代码

```python
def check(y):
    is_prime = [True] * (y + 1)
    prm = []
    is_prime[0], is_prime[1] = False, False
    for i in range(y):
        if is_prime[i]:
            prm.append(i)
        for j in prm:
            if i * j > y: break
            is_prime[i * j] = False
            if not i % j: break
    for i in prm:
        if i * 2 > y: break
        if is_prime[y - i]: print(y, '=', i, '+', y - i, sep='')
    return


x = int(input())
if x < 6 or x % 2 == 1:
    print('Error!')
else:
    check(x)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](M03143-1.jpeg)


## M03247:回文素数

http://cs101.openjudge.cn/pctbook/M03247/

感想：这道题非常体现优化思路的重要性，先处理回文性质后处理素数就可以使复杂度由 $O(n)$ 降至 $O(n/\log{n})$ （还可以利用尾数不为2和5进一步优化常数）；然而我一开始使用先生成素数再判断回文的方法就会面临空间不够和时间超时的两难境地，即使使用了尾数优化也无济于事。说明总体算法的优化永远使最优先的。

代码

```python
#
n=int(input())
maxn=10**(n-1)
sqrtmaxn=10**(n//2+1)
prm=[2]
ans=[]
def check(x):
    for j in prm:
        if j*j>x:break
        if x%j==0: return False
    return True and x!=1

for i in range(3,sqrtmaxn,2):
    if check(i): prm.append(i)
start=max(1,10**(n//2-1))
for i in range(start,sqrtmaxn):
    x=int(str(i)+str(i)[-2::-1])
    if n%2==0: x=int(str(i)+str(i)[::-1])
    if len(str(x))==n  and check(x):
        ans.append(x)
ans.sort()
print(len(ans))
for i in ans:
    print(i,end=' ')

```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)




