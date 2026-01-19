# Assignment #4: T-primes + 贪心

Updated 1814 GMT+8 Sep 30, 2025

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

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：

由小到大排序，只买负价格的商品，优先买最小的。

代码

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(m):
    if a[i] >= 0: break
    ans -= a[i]
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A



思路：

由大到小排序，优先拿最大的硬币，拿到超过剩下的即可

代码

```python
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
tot = sum(a)
num = 0
for i in range(1, n + 1):
    num += a[i - 1]
    if num > tot - num:
        print(i)
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B



思路：

要么每一行都选，要么每一列都选，未选的那一行/列就选n个最小值；两种情况取min

代码

```python
t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=-1
    x=sum(a)+n*min(b)
    y=sum(b)+n*min(a)
    print(min(x,y))
    t-=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### M01017: 装箱问题

greedy, http://cs101.openjudge.cn/pctbook/M01017/


思路：

先将$6*6、5*5、4*4$的物品装进箱子，然后用$1*1$的将$5*5$的空余填满，然后用$2*2$的将$4*4$的空余填满，再有空余填$1*1$；然后填$3*3$，每个箱子可以填4个，有空余类似用小物品填满空隙；最后把$2*2、1*1$的装进箱子。

代码

```python
while True:
    a=list(map(int,input().split()))
    ans=a[5]+a[4]+a[3]
    a[0]=max(0,a[0]-a[4]*11) # NO.5+NO.1 complete
    if a[1]>=a[3]*5:
        a[1]-=a[3]*5 # NO.4+NO.2 complete
    else:
        a[0]=max(0,a[0]-(a[3]*5-a[1])*4) #NO.4+NO.2 completed + NO.1
        a[1]=0
    ans+=a[2]//4
    if a[2]%4:# NO.3 complete
        tmp=7-(a[2]%4)*2
        ans+=1
        if a[1]>=tmp:
            a[1]-=tmp
            a[0]=max(0,a[0]-36+(a[2]%4)*9+tmp*4)
        else:
            a[0] = max(0, a[0] - 36 + (a[2] % 4) * 9 + a[1] * 4)
            a[1]=0
    ans+=a[1]//9
    if a[1]%9:
        ans+=1
        a[0]=max(0,a[0] - 36 + a[1] % 9 *4)
    ans+=a[0]//36+(a[0]%36>0)
    if not ans: break
    print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/



思路：



代码

```python
monthhab = ('pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, '
        'yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu, uayet').split(', ')
tzolkin = ('imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, '
           'chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau').split(', ')
haab = {monthhab[x] : x + 1 for x in range(19)}
def to_tzolkin(x):
    y = max(0, (x - 1) // 260)
    x %= 260
    print(x % 13 if x % 13 else 13, tzolkin[(x + 19) % 20], y, sep = ' ')
    return
m = int(input())
print(m)
for _ in range(m):
    d1, m1, y1 = input().split()
    d = int(d1.rstrip('.')) + 1
    m = haab.get(m1)
    y = int(y1)
    to_tzolkin(d + (m - 1) * 20 + y * 365)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### 230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：

先用欧拉筛将1~10**6以内的素数预处理好，然后对每个ai，它是T-prime当且仅当它是某个素数的平方，采用二分法，找出离sqrt(ai)最近的那个素数；
也可以算出sqrt(ai)，并判定其平方为原数，再用dict字典判断is_prime

代码

```python
is_prime=[1]*1000001
prm=[]
def solve():
    for i in range(2,10**6):
        if is_prime[i]:
            prm.append(i)
        for j in prm:
            if i*j>10**6: break
            is_prime[i*j]=0
            if i%j==0: break
n=int(input())
a=list(map(int,input().split()))
solve()
for i in a:
    l=0
    r=len(prm)-1
    while l<r:
        mid=(l+r)//2
        if prm[mid]**2>=i: r=mid
        else: l=mid+1
    if prm[l]**2==i: print('YES')
    else : print('NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

练习了Greedy（有相当一部分为sort的应用）学习用key和cmp_to_key进行自定义排序；练习了几道简单的matrix题目，主要是练习输入输出，和指标范围判断。
复习了并查集：冰阔落和宗教信仰；（WA因为没看YES还是Yes）
比较大的收获是学习了 defaultdict ：创建时指定一个默认工厂函数（如int、list、set等），当访问不存在的键时，会自动调用这个函数生成默认值，无需手动判断，特别能简化代码的逻辑判断，（如06640倒排索引，用着很方便）。
重做了1366D Two Dividers，学习了题解中用spf数组快速判断的优化方法。
CF上list开10^7居然不会MLE（按一个int 28字节需要300MB），顺便学习了array.array优化内存（实际上是优化到C的int内存大小）

**T12559:最大最小整数**
http://cs101.openjudge.cn/pctbook/T12559/

思路：用cmp_to_key作比较函数，用sort可以方便解决

```python

from functools import cmp_to_key

def compare(a, b):
    if len(a) != len(b):
        return compare(a + b, b + a)
    mn = len(a)
    for i in range(mn):
        if ord(a[i]) < ord(b[i]):
            return -1
        if ord(a[i]) > ord(b[i]):
            return 1
    return -1
n = int(input())
nums = list(input().split())

nums.sort(key=cmp_to_key(compare))
ans=''.join(nums)
ans_=''.join(nums[i] for i in range(n-1,-1,-1))
print(ans_,ans,sep=' ')

```

**1366D：Two Dividers**


```python
import array
#import sys
n = int(input())
a = list(map(int,input().split()))
maxA = max(a)
#spf = list(range(maxA + 1))
spf = array.array('i', range(maxA + 1))
# min prime of i
prm = array.array('i', [])
for i in range(2,maxA + 1):
    if spf[i] == i:
        prm.append(i)
    for j in prm:
        if i * j > maxA: break
        spf[i * j] = j
        if j == spf[i]: break
#print(f"占用内存: {sys.getsizeof(spf) / 2 ** 20} Megabytes")
d1, d2 = [], []
for x in a:
    flag = 0
    i = spf[x]
    tmp = x
    while tmp % i == 0:
        tmp //= i
    if tmp != 1:
        d1.append(tmp)
        d2.append(x // tmp)
    else:
        d1.append(-1)
        d2.append(-1)
print(*d1, sep = ' ')
print(*d2, sep = ' ')
```

![alt text](image-6.png)